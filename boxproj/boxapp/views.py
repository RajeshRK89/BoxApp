
from django.shortcuts import render

from boxsdk import JWTAuth, Client

def index(request):
    file_list = {}
    
    
    

    config = JWTAuth.from_settings_file('/Users/te376346/BoxApp/boxproj/boxapp/771983070_geiglw2s_config.json')

    client = Client(config)

    service_account = client.folder('127019933055')
    files=service_account.get_items()

    # print(file)
    service_account = client.folder('0')
    folders=service_account.get_items()

    # print(file)

    for val in folders:
        # fold_str=('Folder Type: {} - Folder Name: {}').format(val.type,val.id,val.name)
        if val.type == 'folder':
            # print(type(val.id))
            get_files = client.folder(val.id)
            files = get_files.get_items()

            for file_name in files:

                file_str=('File Type: {} - File Name: {} - Belongs to(Folder): {} ').format(file_name.type,file_name.name,val.name)
                file_list['File - '+file_name.id]=file_str
        elif val.type == 'file':
            file_str=('File Type: {} - File Name: {} ').format(val.type,val.name)
            file_list['File - '+val.id]=file_str
        else:
            pass

  
    
    context={'file_list':file_list}
   
    return render(request,'boxtemp/boxapp.html',context)
