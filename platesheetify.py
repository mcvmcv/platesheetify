#! venv/bin/python

import pandas as pd

LCFile			= 'examples/16-0022.txt'
robotFile		= 'robots.txt'
robot			= 'FX'

robotTable		= pd.read_table(robotFile)
robotTable		= robotTable[robotTable['Robot']==robot]
robotTable		= robotTable.set_index('LC Well')

lc				= pd.read_table(LCFile,header=1)
cols			= {'Pos': 'LC Well', 'Group': 'Call'}
lc				= lc.rename(columns=cols)
lc				= lc[['LC Well','Call']]
lc['Plate']		= ''
lc['Well']		= ''
lc				= lc.set_index('LC Well')
lc.update(robotTable)
lc				= lc.reset_index()
sortOrder		= {well: i for i,well in enumerate([l+str(n) for n in range(13) for l in 'ABCDEFGHIJKL'])}
lc['sort']		= lc['Well'].apply(lambda x: sortOrder.get(x),1)
lc				= lc.sort_values('sort')
lc				= lc[['Plate','Well','Call']]
print lc
