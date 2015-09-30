__author__ = 'ashu'
import sys
def get_str(i,j,k,l):
    return str(i)+','+str(j)+'|'+str(k)+','+str(l)
def format(i,j,k,l):
    if(j<i):
        i,j=j,i
    if(l<k):
        k,l=l,k
    if(k<i):
        return str(k)+','+str(l)+'|'+str(i)+','+str(j)
    else:
        return str(i)+','+str(j)+'|'+str(k)+','+str(l)
def write_all_quartets(dt,out_file_path):
    f = open(out_file_path,'w')
    for k in dt.keys():
        for l in dt[k].keys():
            f.write(l+':'+str(dt[k][l])+'\n')
    f.close() 
def quartet_aggregate(path,prefix, suffix, n, g, out_file):
    quartet_dict={}
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range (k+1,n):
                    quartet_dict[frozenset([i,j,k,l])]={get_str(i,j,k,l):0
                                              ,get_str(i,k,j,l):0
                                              ,get_str(i,l,j,k):0}
    for f in range(1,g+1):
        f_in = open(path+'//'+prefix+str(f)+suffix,'r')
        for line in f_in:
            quartet=line.split(':',1)[0]
            siblings=quartet.split('|',1)
            i = int(siblings[0].split(',',1)[0])
            j = int(siblings[0].split(',',1)[1])
            k = int(siblings[1].split(',',1)[0])
            l = int(siblings[1].split(',',1)[1])
            q_set= frozenset([i,j,k,l])
            if q_set in quartet_dict:
                form_q = format(i,j,k,l)
                quartet_dict[q_set][form_q]= quartet_dict[q_set][form_q]+1
        f_in.close()
    write_all_quartets(quartet_dict, path+'//'+out_file)
    
if __name__ == "__main__":
    file_dir=sys.argv[1]
    prefix=sys.argv[2]
    suffix=sys.argv[3]
    num_taxa=sys.argv[4]
    num_genes=sys.argv[5]
    out_filename=sys.argv[6]
    quartet_aggregate(file_dir,prefix,suffix,int(num_taxa),int(num_genes),out_filename)
    
    
