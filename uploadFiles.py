import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
      #  """upload a file to Dropbox using API v2
       # """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.A6-qLuCaX2DyAFwy6wqlqNdg6Y2eoJDOw87eol9tztE9Um9XMa8AILAbDpdWZj1Ea8jLe5ugC_m1-NuH4nX8hiM5Vp6KfHKXN75sTVHvfc9ZRAudooN-Ha-U4ZD25DJjL5QlCOA'
    transferData = TransferData(access_token)

    file_from = r'C:\Users\Rith\OneDrive\Desktop\python\Projects\Project 101\uploadFiles.py'
    file_to = '/python/uploadFiles.py'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
print("your file is uploaded successfully")
if __name__ == '__main__':
    main()

