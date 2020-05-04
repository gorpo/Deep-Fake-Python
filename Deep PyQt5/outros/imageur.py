import pyimgur


"""
Authorization: Client-ID YOUR_CLIENT_ID
client = c06958826c462b4
client secret = d208c0ac25d513edcf33bb2fd684edeaa5c801fb

Exemplo 1----
CLIENT_ID = "ebfc2558bda96e5"
im = pyimgur.Imgur(CLIENT_ID)
image = im.get_image('S1jmapR')
print(image.title) # Cat Ying & Yang
print(image.link)


exemplo 2 ----
CLIENT_ID = "Your_applications_client_id"
PATH = "A Filepath to an image on your computer"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)



"""




CLIENT_ID = "ebfc2558bda96e5"
PATH = 'images/renderizada.jpg'
PATH2 = 'images/logo.png'
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="DEEP FAKE | Pyimageupload")
link1 = uploaded_image.link
uploaded_image_original = im.upload_image(PATH2, title="DEEP FAKE | Pyimageupload")
link2 = uploaded_image_original.link

#print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image_original.link)

#print(uploaded_image.size)
#print(uploaded_image.type)

#<blockquote class="imgur-embed-pub" lang="en" data-id="a/ryxb32b"><a href="//imgur.com/a/ryxb32b">View post on imgur.com</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
