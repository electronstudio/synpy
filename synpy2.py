from synpy2.syncopation import *
import synpy2.PRS as PRS
import synpy2.KTH as KTH
import synpy2.LHL as LHL
import synpy2.SG as SG
import synpy2.TMC as TMC
import synpy2.TOB as TOB
import synpy2.WNBD as WNDB

import fire


#res = calculate_syncopation(PRS,"ab.rhy",outfile="clave.xml")
#print(res)

models = {"PRS": PRS,
"LHL" : LHL,
"SG" : SG,
"TMC" : TMC,
"TOB" : TOB,
"WNBD" : WNDB,
"KTH" : KTH
          }



def syncopation(model,source_file,output_file, parameters=None, barrange=None):
    """calculate_syncopation

     :param str model: LHL, SG, TMC, TOB, WNDB
     :param str source_file: either midi file (.mid) or text file (.rhy)
     :param str output_file: .xml or .json file
     :param str parameters: ???
     :param str barrange: first bar then last bar, e.g. 0 10
    """
    return calculate_syncopation(models[model],source=source_file,parameters=parameters,outfile=output_file, barRange=barrange)



if __name__ == '__main__':
    fire.Fire(syncopation)