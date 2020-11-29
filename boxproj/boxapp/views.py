
from django.shortcuts import render



def index(request):
    file_list = {}
    from boxsdk import JWTAuth, Client
    
    

    config = JWTAuth.from_settings_file('/Users/te376346/BoxApp/boxproj/boxapp/771983070_geiglw2s_config.json')

    client = Client(config)

    service_account = client.folder('127019933055')
    files=service_account.get_items()

    # print(file)

    for val in files:
        tot_str=('File Type: {} - File ID: {} - File Name: {}').format(val.type,val.id,val.name)
        
        file_list[val.id]=tot_str
        # print(val.id, val.name , val.type )
    print(file_list)
    
    context={'file_list':file_list}
   
    return render(request,'boxtemp/boxapp.html',context)
