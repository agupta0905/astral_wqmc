__author__ = 'ashu'
import sys
from quartet_aggregate import formatted
def write(dict,file):
    f=open(file,'w')
    for k in dict.keys():
        f.write(k+':'+str(dict[k])+'\n')
    f.close()
def get_taxa(q):
    siblings = q.split('|',1)
    i,j = siblings[0].split(',',1)[:]
    k,l = siblings[1].split(',',1)[:]
    return [i,j,k,l]
def adjust_quartet_weight(mdir,r,g,t):
    w=[1, 5, 10, 25, 50]
    dict_list=map(lambda x: {}, w)
    for i in range(1,g+1):
        q_dict={}
        f=open(mdir+'/R'+r+'/'+str(i)+'/allorigbin_t_'+str(t)+'_quartets_relabeled.txt','r')
        for line in f:
            q=line.split(':',1)[0]
            v=int(line.split(':',1)[1].replace('\n',''))
            q_dict[q]=v
        f.close()
        del dict_list
        dict_list=[]
        for k in range(0,len(w)):
            dict_list.append(q_dict.copy())
        f=open(mdir+'/R'+r+'/'+str(i)+'/quartets_relabeled.txt','r')
        for line in f:
            qlist=get_taxa(line.split(':',1)[0])
            q=formatted(qlist[0],qlist[1],qlist[2],qlist[3])
            v=int(line.split(':',1)[1].replace('\n',''))
            for idx,weight in enumerate(w):
                dict_list[idx][q]=dict_list[idx][q]-v+weight*v
        f.close()
        for idx,weight in enumerate(w):
            write(dict_list[idx],mdir+'/R'+r+'/'+str(i)+'/allorigbin_t_'+str(t) +'_quartets_relabeled_'+'_w_'+str(weight)+'.txt')  
        print "Gene-",i," Done" 
if __name__ == "__main__":
    model_dir=sys.argv[1]
    replicate=sys.argv[2]
    num_genes=int(sys.argv[3])
    threshold=int(sys.argv[4])
    adjust_quartet_weight(model_dir,replicate,int(num_genes),threshold)
    
    
