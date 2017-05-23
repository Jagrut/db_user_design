from django.shortcuts import render
import sqlite3
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from collections import defaultdict
# Create your views here.
def get_user_permissions(request,user_id):
    message = ''
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        data = defaultdict(list)
        for row in c.execute('select permission from user_design_permissions                                                                      where id in( select perm_id from user_design_user_permissions                                                        where role_id in (select role_id from user_design_user                                                               join user_design_user_roles on user_design_user.id='+user_id+'                                                       and user_design_user_roles.user_id='+user_id+'))'):
            print(row[0])
            data[user_id].append(row[0])
        conn.commit()
        message = data
    except Exception as e:
        message = e
    finally:
        conn.close()
        return JsonResponse({'message':message})

def checkpermission(request):
    user_id = int(request.GET['userid'])
    perm_id = int(request.GET['permissionid'])
    message = ''
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        inside = 0
        for row in c.execute('select id from user_design_permissions                                                                              where id in( select perm_id from user_design_user_permissions                                                        where role_id in (select role_id from user_design_user                                                               join user_design_user_roles on user_design_user.id='+str(user_id)+'                                                  and user_design_user_roles.user_id='+str(user_id)+'))'):
            if row[0] == perm_id:
                inside = 1
                message = str(user_id)+' is having a permission '+str(perm_id)
        if inside == 0:
            message = str(user_id)+' is not having a permission '+str(perm_id)
        conn.commit()
    except Exception as e:
        message = e
    finally:
        conn.close()
        return JsonResponse({'message':message})


@csrf_exempt
def deletepermission(request, permission_id):
    message = ''
    import pdb;pdb.set_trace()
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        obj = c.execute('select * from user_design_permissions where id='+str(permission_id))
        if not obj.fetchone()==None:
            c.execute('delete from user_design_permissions where id='+str(permission_id))
            message = 'permission '+str(permission_id)+' deleted successfully'
        else:
            message = 'permission '+str(permission_id)+' does not exist'
        conn.commit()
    except Exception as e:
        message = e
    finally:
        conn.close()
        return JsonResponse({'message':message})

@csrf_exempt
def update_permission(request, role_id):
    post_dict = json.loads(request.body.decode("utf-8"))
    permission_arr = list(map(int, post_dict['permissions']))
    message = ''
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('delete from user_design_user_permissions where role_id='+role_id)
        conn.commit()
        arr = []
        for permission in permission_arr:
            arr.append((permission, int(role_id)))
        c.executemany('insert into user_design_user_permissions (perm_id,role_id) values (?,?)', arr)
        conn.commit()
        message = 'permission updated successfully' 
    except Exception as e:
        message = e
    finally:
        conn.close()
        return JsonResponse({'message':message})
