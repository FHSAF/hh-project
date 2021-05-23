from django.shortcuts import redirect, render
from django.http import request
import requests 
import re
from bs4 import BeautifulSoup

from .models import Site, Page

def Index(request):

    sites = Site.objects.all().order_by('-created_at')
    pages = Page.objects.all()
    template_dir = 'pages/index.htm'
    context = {
        'sites': sites,
        'pages': pages
    }
    return render(request, template_dir, context)

def parser(request):
    if request.method == 'POST':
        print('--------------------------->the method is post!')
        url = request.POST.get('url')
        name = request.POST.get('name')
        outPutFileName = name
        page_source = requests.get(url, 'html.parser')

        # with open(outPutFileName, 'w') as f:
        #     f.write(page_source.text)
        #     f.close

        
        site = Site.objects.create(
            url=url,
            name=name
        )
        site.save()

        pages_list = re.findall('(?<=href=")(.*)(?=\A")', page_source.text)
        print(pages_list)

        # title = re.compile('(?<=<title>)(.*)(?=</title>)')
        title_re = re.findall('(?<=<title>)(.*)(?=</title>)', page_source.text)
        title = ''.join(title_re)

        page = Page.objects.create(
            site = site,
            content = page_source.text,
            title = title
        )
        page.save()
    template_dir = 'forms/site.htm'
    context = {
        'text': 'text',
    }
    return render(request, template_dir, context)

def details(request, pk):
    site = Site.objects.filter(id=pk).first()
    
    pages = Page.objects.all().filter(site=site)
    template_dir = 'pages/details.htm'
    context = {
        'site': site,
        'pages': pages
    }
    return render(request, template_dir, context)


def aparser(request):
    if request.method == 'POST':
        # values from form
        url = request.POST.get('url')
        name = request.POST.get('name')
        # 
        page_source = requests.get(url)
        site_bs4 = BeautifulSoup(page_source.content, 'html.parser')
        
        
        site = Site.objects.create(
            url=url,
            name=name
        )
        site.save()

        # pages_list = re.findall('(?<=href=")(.*)(?=\A")', page_source.text)
        # print(pages_list)

        title = re.compile('(?<=<title>)(.*)(?=</title>)')
        title_re = re.findall('(?<=<title>)(.*)(?=</title>)', page_source.text)
        title = ''.join(title_re)

        page = Page.objects.create(
                site = site,
                uri = url,
                content = site_bs4.prettify(),
                title = title
            )
        page.save()
        title = site_bs4.find_all('title')

        amount = 0
        for a_tag in site_bs4.find_all('a', href=True):

            if amount == 20:
                return redirect('/')
            if '/' not in a_tag['href']:
                print('--------------------->', a_tag['href'])
                continue
            if len(a_tag['href']) < 2:
                print('>>>>>>>>>>>>>>>>>>>>>', a_tag['href'])
                continue
            
            amount += 1
            try:
                
                page_source = requests.get(url+a_tag['href'])
                site_bs4 = BeautifulSoup(page_source.content, 'html.parser')
                # title = re.compile('(?<=<title>)(.*)(?=</title>)')
                title_re = re.findall('(?<=<title>)(.*)(?=</title>)', page_source.text)
                title = ''.join(title_re)
                page = Page.objects.create(
                    site = site,
                    uri = url+a_tag['href'],
                    content = site_bs4.prettify(),
                    title = title,
                )
                page.save()
            except:
                print()
                print(a_tag['href'])
                print()
                continue
        return redirect('/')
    template_dir = 'forms/use_soup.htm'
    context = {
        'text': 'text',
    }
    return render(request, template_dir, context)
