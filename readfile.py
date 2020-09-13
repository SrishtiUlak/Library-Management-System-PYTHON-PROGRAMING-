def read_file(path):
    file = open(path,"r")
    content  = file.readlines()
    return content
def content_list2d(unpr_list):
    db = []
    for i in unpr_list:
        db.append(i.replace("\n","").replace("$","").split(","))
    return db

def main_db(path):
    db = content_list2d(read_file(path))
    return db

    



