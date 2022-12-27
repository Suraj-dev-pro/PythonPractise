#file object practise corey schafer
with open('dalle2space.png','rb') as rf:
    with open('dallespace_copy.png','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
    

    
    #while len(f_contents)>0:
    #    print(f_contents,end='*')
    #    f_contents = f.read(size_to_read)
        