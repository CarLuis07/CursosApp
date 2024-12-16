from django.shortcuts import render

def index(request):
    listaArticulos = [
        {'title': 'Primer Blog', 
         'autor': 'Luis Cardona',
         'image': 'https://edteam-media.s3.amazonaws.com/blogs/original/511e1605-3a2a-46ba-a211-ff5d33d6028f.png'},
        {'title': 'segundo Blog', 
         'autor': 'Luis Cardona',
         'image': 'https://edteam-media.s3.amazonaws.com/blogs/original/b412d87c-b524-49e3-93ff-403fe79b1f54'},
        {'title': 'Tercer Blog', 
         'autor': 'Luis Cardona',
         'image': 'https://edteam-media.s3.amazonaws.com/blogs/original/965780b1-7a4c-442c-8fe8-53d5e913da95.png'},
         
    ]

    context = {
        'articulos': listaArticulos
    }

    return render(request, 'index.html', context)