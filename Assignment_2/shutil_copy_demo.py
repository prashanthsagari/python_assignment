import shutil

shutil.copy('source.txt', 'destination.txt')
# test_dir folder must present other wise it throws error
shutil.copy('source.txt', 'test_dir/')

# backup directory must be present
shutil.copy2("source.txt", "backup/")  
shutil.copy2("source.txt", "destination2.txt") 

# Only copies content, nothing else
shutil.copyfile("source.txt", "destination3.txt") 