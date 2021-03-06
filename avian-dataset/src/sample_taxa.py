__author__ = 'ashu'
import sys
import dendropy
from random import shuffle
def sample_helper(truetreefile,estimatedtreefile,s):
    #print truetreefile
    #print estimatedtreefile
    tt=dendropy.Tree.get(
        path=truetreefile,
        schema='newick')
    te=dendropy.Tree.get(
        path=estimatedtreefile,
        schema='newick')
    tlist=tt.taxon_namespace.labels()
    shuffle(tlist)
    tlist=tlist[0:s]
    #print tlist
    tt.retain_taxa_with_labels(tlist)
    te.retain_taxa_with_labels(tlist)
    #print truetreefile+'_sampled_'+str(s)
    ft = open(truetreefile+'_sampled_'+str(s),'w')
    ft.write(tt.as_string('newick'))
    ft.close()
    fe = open(estimatedtreefile+'_sampled_'+str(s),'w')
    fe.write(te.as_string('newick'))
    fe.close()
def sample_taxa(path, r, g, s):
    tpath=path+'-true'
    for i in range(1,g+1):
        sample_helper(tpath+'/R'+r+'/'+str(i)+'/true.gt',
            path+'/R'+r+'/'+str(i)+'/raxmlboot.gtrgamma/RAxML_bipartitions.final.f200', s)
        print i
if __name__ == "__main__":
    modeldir=sys.argv[1]
    replicate=sys.argv[2]
    numgenes=int(sys.argv[3])
    samplesize=int(sys.argv[4])
    sample_taxa(modeldir, replicate, numgenes, samplesize)    
    
