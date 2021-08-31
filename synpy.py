# -*- coding: utf-8 -*-

from synpy2.syncopation import *
import synpy2.PRS as PRS
import synpy2.KTH as KTH
import synpy2.LHL as LHL
import synpy2.SG as SG
import synpy2.TMC as TMC
import synpy2.TOB as TOB
import synpy2.WNBD as WNDB

import fire
from gooey import Gooey, GooeyParser

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




@Gooey()
def main():
    parser = GooeyParser(description='Calculate Syncopation')

    parser.add_argument(
        'model',
        metavar='Model to use',
        help='Models: KTH, LHL, PRS, SG, TMC, TOB, WNDB',
        default="KTH",
        choices=['KTH', 'LHL', 'PRS', 'SG', 'TMC', 'TOB', 'WNDB']
    )

    parser.add_argument(
        'source_file',
        widget='FileChooser',
        metavar='Source file',
        help='either midi file (.mid) or text file (.rhy)',
        default="Rhythm_stimuli_text_format/ab.rhy"
    )

    parser.add_argument(
        'output_file',
        widget='FileSaver',
        metavar='Output file',
        help='.xml or .json file',
        default="output.json"
    )

    parser.add_argument(
        '--parameters',
        help='???',
        default=None
    )

    parser.add_argument(
        '--bar_range',
        metavar='first_bar last_bar',
        help= 'e.g. 0 10',
        default=None
    )

    args = parser.parse_args()

    #print(args.model)

    #print(type(models[args.model]), type(args.source_file), type(args.output_file))
    #calculate_syncopation(models[args.model],source="Raw_rating_data/ab.rhy",outfile=args.output_file)
    range = None
    if args.bar_range:
        range = list(map(int,list(args.bar_range.split())))
        print("bar range is ", range)
    r = calculate_syncopation(models[args.model], source=args.source_file, outfile=args.output_file, parameters=args.parameters, barRange=range)#barRange=args.bar_range)
    for key, value in r.items():
        print(str(key) + " : " + str(value))
        #print(key, ' : ', value)
        #print(value)

if __name__ == '__main__':
    #calculate_syncopation(models["KTH"],source="Raw_rating_data/ab.rhy",outfile="clave.xml", parameters=None, barRange=None)
    main()

#if __name__ == '__main__':
#    fire.Fire(syncopation)