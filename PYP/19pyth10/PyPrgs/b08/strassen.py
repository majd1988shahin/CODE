import sys,os,io
s=r'[{\"[\w]*\": \"[\w]*\", \"[\w]*\": \"[\w]*\", \"[\w]*\": {\"[\w]*\": \"[\w]*\", \"[\w]*\": \"[\w]*\", \"[\w]*\": \"[\w]*\", \"[\w]*\": \"[\w]*\", "strassenname": "([\w-])", \"[\w]*\": \"[\w]*\", \"[\w]*\": \"[\w]*\", \"[\w]*\": \"[[\w]*]\", \"[\w]*\": \"[\w]*\", \"[\w]*\": \"[\w]*\"}, \"[\w]*\": \"[\w]*\"}'
s=r'\[\{[^[\{\}]*]*\{\"strassenname\":\"([\w\s]*)[^[\{\}]*]*\}\}\]'
def main():    
    if "strassenma.json" not in os.listdir(os.getcwd()):
        print("strassenma.json muss heruntergeladen werden")
        import urllib.request
        url = 'https://mannheim.opendatasoft.com/explore/dataset/strassennamen-in-mannheim/download/?format=json&timezone=Europe/Berlin'
        response = urllib.request.urlopen(url)
        data = response.read()      # a `bytes` object
        text = data.decode()
        n=len(text)
        print(text[0:178])
        with io.open("strassenma.json","w") as f:
            f.write(text)

    else:
        print("strassenma.json  ist schon da")
        with io.open("strassenma.json","r") as f:
            print(f.read()[:2000])
    
    
    pass


if __name__=="__main__":
    main()