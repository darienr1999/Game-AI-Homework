""#line:17
import sys ,pygame ,math ,numpy ,random ,time ,copy #line:19
from pygame .locals import *#line:20
from constants import *#line:22
from utils import *#line:23
from core import *#line:24
def f33 (OOO00OO00O00000OO ,OO000O000OO0OO000 ):#line:27
	if (OOO00OO00O00000OO [0 ]!=OO000O000OO0OO000 [0 ]):#line:30
		OO00OO00OO00OOOO0 =(OOO00OO00O00000OO [1 ]-OO000O000OO0OO000 [1 ])/float (OOO00OO00O00000OO [0 ]-OO000O000OO0OO000 [0 ])#line:31
		return OO00OO00OO00OOOO0 #line:32
	else :#line:33
		return None #line:34
def f32 (OO00OO00O00OOO00O ,O00000OO00OOOO0OO ):#line:37
	return OO00OO00O00OOO00O [1 ]-(O00000OO00OOOO0OO *OO00OO00O00OOO00O [0 ])#line:38
def f31 (O00O0OOOOOOOO0O0O ,O00OO00OO0OO0OO00 ,O0O000OOO0OO0OOO0 ,O0OO00O0O0O0O0OO0 ):#line:46
	OOOO0OOO00OOO0OO0 =f33 (O00O0OOOOOOOO0O0O ,O00OO00OO0OO0OO00 )#line:47
	OOOO0000O00O0000O =f33 (O0O000OOO0OO0OOO0 ,O0OO00O0O0O0O0OO0 )#line:48
	if (OOOO0OOO00OOO0OO0 !=OOOO0000O00O0000O ):#line:51
		if (OOOO0OOO00OOO0OO0 is not None and OOOO0000O00O0000O is not None ):#line:55
			OOOOOO0O00O00OOOO =f32 (O00O0OOOOOOOO0O0O ,OOOO0OOO00OOO0OO0 )#line:57
			O0000OO0OOO0O0O0O =f32 (O0O000OOO0OO0OOO0 ,OOOO0000O00O0000O )#line:58
			OO0O00OO0000OOO0O =(O0000OO0OOO0O0O0O -OOOOOO0O00O00OOOO )/float (OOOO0OOO00OOO0OO0 -OOOO0000O00O0000O )#line:59
			O000O00OOO0OO00O0 =(OOOO0OOO00OOO0OO0 *OO0O00OO0000OOO0O )+OOOOOO0O00O00OOOO #line:60
		else :#line:61
			if (OOOO0OOO00OOO0OO0 is None ):#line:63
				O0000OO0OOO0O0O0O =f32 (O0O000OOO0OO0OOO0 ,OOOO0000O00O0000O )#line:64
				OO0O00OO0000OOO0O =O00O0OOOOOOOO0O0O [0 ]#line:65
				O000O00OOO0OO00O0 =(OOOO0000O00O0000O *OO0O00OO0000OOO0O )+O0000OO0OOO0O0O0O #line:66
			elif (OOOO0000O00O0000O is None ):#line:68
				OOOOOO0O00O00OOOO =f32 (O00O0OOOOOOOO0O0O ,OOOO0OOO00OOO0OO0 )#line:69
				OO0O00OO0000OOO0O =O0O000OOO0OO0OOO0 [0 ]#line:70
				O000O00OOO0OO00O0 =(OOOO0OOO00OOO0OO0 *OO0O00OO0000OOO0O )+OOOOOO0O00O00OOOO #line:71
			else :#line:72
				assert false #line:73
		return ((OO0O00OO0000OOO0O ,O000O00OOO0OO00O0 ),)#line:75
	else :#line:76
		OOOOOO0O00O00OOOO ,O0000OO0OOO0O0O0O =None ,None #line:81
		if OOOO0OOO00OOO0OO0 is not None :#line:82
			OOOOOO0O00O00OOOO =f32 (O00O0OOOOOOOO0O0O ,OOOO0OOO00OOO0OO0 )#line:83
		if OOOO0000O00O0000O is not None :#line:85
			O0000OO0OOO0O0O0O =f32 (O0O000OOO0OO0OOO0 ,OOOO0000O00O0000O )#line:86
		if OOOOOO0O00O00OOOO ==O0000OO0OOO0O0O0O :#line:89
			return O00O0OOOOOOOO0O0O ,O00OO00OO0OO0OO00 ,O0O000OOO0OO0OOO0 ,O0OO00O0O0O0O0OO0 #line:90
		else :#line:91
			return None #line:92
def f30 (O0OO00O00OO0OOOOO ,O000OO0OOO0O00OO0 ,OO00O0OOO0O000000 ):#line:94
	return O0OO00O00OO0OOOOO +EPSILON >=min (O000OO0OOO0O00OO0 ,OO00O0OOO0O000000 )and O0OO00O00OO0OOOOO -EPSILON <=max (O000OO0OOO0O00OO0 ,OO00O0OOO0O000000 )#line:95
def f29 (O00OOOOOO0O00O00O ,OOOOOOOOO0OOO0000 ,O0OOOO0O00O000O0O ,OOO000O00O00O0OOO ):#line:103
	OO0OOO0O00OOO0000 =f31 (O00OOOOOO0O00O00O ,OOOOOOOOO0OOO0000 ,O0OOOO0O00O000O0O ,OOO000O00O00O0OOO )#line:104
	if OO0OOO0O00OOO0000 is not None :#line:105
		OO0OOO0O00OOO0000 =OO0OOO0O00OOO0000 [0 ]#line:106
		if f30 (OO0OOO0O00OOO0000 [0 ],O00OOOOOO0O00O00O [0 ],OOOOOOOOO0OOO0000 [0 ])and f30 (OO0OOO0O00OOO0000 [1 ],O00OOOOOO0O00O00O [1 ],OOOOOOOOO0OOO0000 [1 ])and f30 (OO0OOO0O00OOO0000 [0 ],O0OOOO0O00O000O0O [0 ],OOO000O00O00O0OOO [0 ])and f30 (OO0OOO0O00OOO0000 [1 ],O0OOOO0O00O000O0O [1 ],OOO000O00O00O0OOO [1 ]):#line:107
			return OO0OOO0O00OOO0000 #line:108
	return None #line:109
def f15 (OOO0000O00O0OO0O0 ,O00000O0OO0000000 ):#line:111
	return (((O00000O0OO0000000 [0 ]-OOO0000O00O0OO0O0 [0 ])**2 )+((O00000O0OO0000000 [1 ]-OOO0000O00O0OO0O0 [1 ])**2 ))**0.5 #line:112
def f28 (O000000O0OOOO000O ,O0OO000OO00O0O0OO ,O00O0O0OOO0O0O0O0 ):#line:114
	return f29 (O00O0O0OOO0O0O0O0 [0 ],O00O0O0OOO0O0O0O0 [1 ],O000000O0OOOO000O ,O0OO000OO00O0O0OO )#line:115
def f13 (OOOOO0000OO00OO0O ,OO00O0O0O0OOO0OOO ,OOOOOO00O0O0OO0O0 ):#line:118
	for O0O00O0OOO0OOO0OO in OOOOOO00O0O0OO0O0 :#line:119
		OO0OOO00OOOO0OO00 =f28 (OOOOO0000OO00OO0O ,OO00O0O0O0OOO0OOO ,O0O00O0OOO0OOO0OO )#line:120
		if OO0OOO00OOOO0OO00 !=None :#line:121
			return OO0OOO00OOOO0OO00 #line:122
	return None #line:123
def f12 (O00OOO0O00000O00O ,O0OOO0OOOO0OOO0O0 ):#line:125
	OOO0000O000OOO000 =f15 (O00OOO0O00000O00O [1 ],O00OOO0O00000O00O [0 ])**2.0 #line:126
	if OOO0000O000OOO000 ==0.0 :#line:127
		return f15 (O0OOO0OOOO0OOO0O0 ,O00OOO0O00000O00O [0 ])#line:128
	O0OOO0OO0OO00OO00 =(O0OOO0OOOO0OOO0O0 [0 ]-O00OOO0O00000O00O [0 ][0 ],O0OOO0OOOO0OOO0O0 [1 ]-O00OOO0O00000O00O [0 ][1 ])#line:132
	OO00O00O00OO0O0O0 =(O00OOO0O00000O00O [1 ][0 ]-O00OOO0O00000O00O [0 ][0 ],O00OOO0O00000O00O [1 ][1 ]-O00OOO0O00000O00O [0 ][1 ])#line:133
	OO00OOOO00O0OO000 =dotProduct (O0OOO0OO0OO00OO00 ,OO00O00O00OO0O0O0 )/OOO0000O000OOO000 #line:134
	if OO00OOOO00O0OO000 <0.0 :#line:135
		return f15 (O0OOO0OOOO0OOO0O0 ,O00OOO0O00000O00O [0 ])#line:136
	elif OO00OOOO00O0OO000 >1.0 :#line:137
		return f15 (O0OOO0OOOO0OOO0O0 ,O00OOO0O00000O00O [1 ])#line:138
	OOOO0O0O0O000OO00 =(O00OOO0O00000O00O [0 ][0 ]+(OO00OOOO00O0OO000 *(O00OOO0O00000O00O [1 ][0 ]-O00OOO0O00000O00O [0 ][0 ])),O00OOO0O00000O00O [0 ][1 ]+(OO00OOOO00O0OO000 *(O00OOO0O00000O00O [1 ][1 ]-O00OOO0O00000O00O [0 ][1 ])))#line:139
	return f15 (O0OOO0OOOO0OOO0O0 ,OOOO0O0O0O000OO00 )#line:140
def f20 (O00OOOOO0OOO0OO0O ,O0O0OO0O0O000O0O0 ,O000OO0O0OO0O00O0 ):#line:143
	OOO0O00O0OO0OOOOO =None #line:144
	OO0OO000000O0O0OO =INFINITY #line:145
	for OO0OOO0OOO0OOO00O in O0O0OO0O0O000O0O0 :#line:146
		if f13 (O00OOOOO0OOO0OO0O ,OO0OOO0OOO0OOO00O ,O000OO0O0OO0O00O0 )==None :#line:147
			OO00O0000000O00O0 =f15 (O00OOOOO0OOO0OO0O ,OO0OOO0OOO0OOO00O )#line:148
			if OOO0O00O0OO0OOOOO ==None or OO00O0000000O00O0 <OO0OO000000O0O0OO :#line:149
				OOO0O00O0OO0OOOOO =OO0OOO0OOO0OOO00O #line:150
				OO0OO000000O0O0OO =OO00O0000000O00O0 #line:151
	return OOO0O00O0OO0OOOOO #line:152
class AStarNavigator2 (PathNetworkNavigator ):#line:159
	def computePath (OOOOO000O0OOOO0O0 ,O000OOOOO0O0O0OO0 ,O000OO000OO000O0O ):#line:166
		OOOOO000O0OOOO0O0 .setPath (None )#line:167
		if OOOOO000O0OOOO0O0 .agent !=None and OOOOO000O0OOOO0O0 .world !=None :#line:169
			OOOOO000O0OOOO0O0 .source =O000OOOOO0O0O0OO0 #line:170
			OOOOO000O0OOOO0O0 .destination =O000OO000OO000O0O #line:171
			if f22 (O000OOOOO0O0O0OO0 ,O000OO000OO000O0O ,OOOOO000O0OOOO0O0 .world .getLinesWithoutBorders (),OOOOO000O0OOOO0O0 .world .getPoints (),OOOOO000O0OOOO0O0 .agent ):#line:175
				OOOOO000O0OOOO0O0 .agent .moveToTarget (O000OO000OO000O0O )#line:176
			else :#line:177
				O0O000000OOO0O00O =f21 (O000OOOOO0O0O0OO0 ,OOOOO000O0OOOO0O0 .pathnodes ,OOOOO000O0OOOO0O0 .world .getLinesWithoutBorders (),OOOOO000O0OOOO0O0 .agent )#line:180
				OO000O0O00OO0O0O0 =f21 (O000OO000OO000O0O ,OOOOO000O0OOOO0O0 .pathnodes ,OOOOO000O0OOOO0O0 .world .getLinesWithoutBorders (),OOOOO000O0OOOO0O0 .agent )#line:181
				if O0O000000OOO0O00O !=None and OO000O0O00OO0O0O0 !=None :#line:182
					O0OOO00OO0O00O000 =f23 (OOOOO000O0OOOO0O0 .pathnetwork ,OOOOO000O0OOOO0O0 .world .getGates (),OOOOO000O0OOOO0O0 .world )#line:184
					O00O0O00O00O0O0OO =[]#line:185
					OOOO00O00000OOO0O ,O00O0O00O00O0O0OO =f17 (O0O000000OOO0O00O ,OO000O0O00OO0O0O0 ,O0OOO00OO0O00O000 )#line:187
					if OOOO00O00000OOO0O is not None and len (OOOO00O00000OOO0O )>0 :#line:188
						OOOO00O00000OOO0O =f27 (O000OOOOO0O0O0OO0 ,O000OO000OO000O0O ,OOOO00O00000OOO0O ,OOOOO000O0OOOO0O0 .world ,OOOOO000O0OOOO0O0 .agent )#line:190
						OOOOO000O0OOOO0O0 .setPath (OOOO00O00000OOO0O )#line:192
						if OOOOO000O0OOOO0O0 .path is not None and len (OOOOO000O0OOOO0O0 .path )>0 :#line:193
							OO0000OO0000O0OOO =OOOOO000O0OOOO0O0 .path .pop (0 )#line:195
							OOOOO000O0OOOO0O0 .agent .moveToTarget (OO0000OO0000O0OOO )#line:196
		return None #line:197
	def checkpoint (O00000O0OO0OOOOOO ):#line:201
		f26 (O00000O0OO0OOOOOO )#line:202
		return None #line:203
	def smooth (O0O0O0O0OOO0O00O0 ):#line:207
		return f24 (O0O0O0O0OOO0O00O0 )#line:208
	def update (O0O0OO00O0OOO00OO ,O0O0O0OO00O0000OO ):#line:210
		f25 (O0O0OO00O0OOO00OO ,O0O0O0OO00O0000OO )#line:211
def f23 (O00O00O00OO0OOO0O ,O0O0O0OO0OO000O0O ,OOO00O0OO00O0O0O0 ):#line:215
	OO00OO0O00OOOOO00 =[]#line:216
	for OO0OO000OOO0OOO00 in O00O00O00OO0OOO0O :#line:217
		O0O000000O0000000 =f13 (OO0OO000OOO0OOO00 [0 ],OO0OO000OOO0OOO00 [1 ],O0O0O0OO0OO000O0O )#line:218
		if O0O000000O0000000 ==None :#line:219
			OO00OO0O00OOOOO00 .append (OO0OO000OOO0OOO00 )#line:220
	return OO00OO0O00OOOOO00 #line:221
def f22 (OO00O0OO00O0OOOOO ,O00OO00OOO00OOOOO ,O0O0O000OOOO0000O ,OO0O0O00O0000OOO0 ,O0O000OOOO000000O ):#line:230
    #O000OOO0O0O0O0OOO =O0O000OOOO000000O .getMaxRadius ()#line:232
    #O0OOO0OO00OOOOO00 =f13 (OO00O0OO00O0OOOOO ,O00OO00OOO00OOOOO ,O0O0O000OOOO0000O )#line:233
    #if O0OOO0OO00OOOOO00 is None :#line:234
    #    O0000O0000OO00OOO =False #line:235
    #    for O0OOO0000O000O00O in OO0O0O00O0000OOO0 :#line:236
    #        if f12 ((OO00O0OO00O0OOOOO ,O00OO00OOO00OOOOO ),O0OOO0000O000O00O )<O000OOO0O0O0O0OOO :#line:237
    #            O0000O0000OO00OOO =True #line:238
    #    if not O0000O0000OO00OOO :#line:239
    #        return True #line:240
    return False #line:242
def f21 (O0OOOOOOOO0O00OOO ,O00O0O0OOO0O0000O ,OOOO0OOOOO00OOOO0 ,OO0OO00O00O00OOOO ):#line:249
	OO000O00OOO0O0OO0 =None #line:250
	OO000O00OOO0O0OO0 =f20 (O0OOOOOOOO0O00OOO ,O00O0O0OOO0O0000O ,OOOO0OOOOO00OOOO0 )#line:252
	return OO000O00OOO0O0OO0 #line:254
def f18 (OO000O0O0O000O0O0 ,OO000OO00O0O00OO0 ,func =lambda O0O00OOOO00O00000 :O0O00OOOO00O00000 ):#line:257
	for OOOOOO0O0O000O0O0 in range (len (OO000OO00O0O00OO0 )):#line:258
		if func (OO000O0O0O000O0O0 )<func (OO000OO00O0O00OO0 [OOOOOO0O0O000O0O0 ]):#line:259
			OO000OO00O0O00OO0 .insert (OOOOOO0O0O000O0O0 ,OO000O0O0O000O0O0 )#line:260
			return OO000OO00O0O00OO0 #line:261
	OO000OO00O0O00OO0 .append (OO000O0O0O000O0O0 )#line:262
	return OO000OO00O0O00OO0 #line:263
def f17 (O0O000OO0OOOOOOOO ,OO0O000OO0O0O00OO ,OOO00OO000O0O0O00 ):#line:273
	OOO00O0OOOO00O0O0 =[]#line:274
	OOO0O00OOO00OOO00 =[]#line:275
	O00OOO000O00OOO00 =[]#line:276
	O0O000OO0OOOOOOOO =(O0O000OO0OOOOOOOO ,0 ,f15 (O0O000OO0OOOOOOOO ,OO0O000OO0O0O00OO ),None )#line:279
	O00OOO000O00OOO00 =set ()#line:280
	OOOOO0OOO0O0000O0 =set ()#line:281
	OOO0O00OOO00OOO00 =[O0O000OO0OOOOOOOO ]#line:282
	OO0OO000OOOOO000O =O0O000OO0OOOOOOOO #line:283
	while OO0OO000OOOOO000O is not None and OO0OO000OOOOO000O [0 ]!=OO0O000OO0O0O00OO and len (OOO0O00OOO00OOO00 )>0 :#line:286
		O00OOO000O00OOO00 .add (OO0OO000OOOOO000O [0 ])#line:287
		OOOOO0OOO0O0000O0 .add (OO0OO000OOOOO000O )#line:288
		OOO0O00OOO00OOO00 .pop (0 )#line:289
		OO0O0O0OO0000OOOO =f16 (OO0OO000OOOOO000O ,OOO00OO000O0O0O00 ,OO0O000OO0O0O00OO )#line:290
		for OO00OO0000O00OO00 in OO0O0O0OO0000OOOO :#line:291
			if OO00OO0000O00OO00 [0 ]not in O00OOO000O00OOO00 :#line:292
				f18 (OO00OO0000O00OO00 ,OOO0O00OOO00OOO00 ,lambda O0OOO0000OOO0000O :O0OOO0000OOO0000O [1 ]+O0OOO0000OOO0000O [2 ])#line:293
		if len (OOO0O00OOO00OOO00 )>0 :#line:294
			OO0OO000OOOOO000O =OOO0O00OOO00OOO00 [0 ]#line:295
		else :#line:296
			OO0OO000OOOOO000O =None #line:297
	if OO0OO000OOOOO000O is not None :#line:300
		while OO0OO000OOOOO000O [3 ]is not None :#line:301
			OOO00O0OOOO00O0O0 .append (OO0OO000OOOOO000O [0 ])#line:302
			O000OOOOOO0OO00OO =OO0OO000OOOOO000O [3 ]#line:303
			for O00O000OO00O0OOO0 in list (OOOOO0OOO0O0000O0 ):#line:304
				if O000OOOOOO0OO00OO ==O00O000OO00O0OOO0 [0 ]:#line:305
					OO0OO000OOOOO000O =O00O000OO00O0OOO0 #line:306
					break #line:307
		OOO00O0OOOO00O0O0 .append (OO0OO000OOOOO000O [0 ])#line:308
		OOO00O0OOOO00O0O0 .reverse ()#line:309
	O00OOO000O00OOO00 =list (O00OOO000O00OOO00 )#line:310
	return OOO00O0OOOO00O0O0 ,O00OOO000O00OOO00 #line:312
def f16 (O000000O0OO0O0000 ,O0O0000O0OO0O00OO ,OO0O0O0O0O0O0O0OO ):#line:315
	O0OO0OOOOOO0000OO =[]#line:316
	for OOOOO00OOOOOOOOO0 in O0O0000O0OO0O00OO :#line:317
		if OOOOO00OOOOOOOOO0 [0 ]==O000000O0OO0O0000 [0 ]:#line:318
			O0OO0OOOOOO0000OO .append ((OOOOO00OOOOOOOOO0 [1 ],O000000O0OO0O0000 [1 ]+f15 (OOOOO00OOOOOOOOO0 [0 ],OOOOO00OOOOOOOOO0 [1 ]),f15 (OOOOO00OOOOOOOOO0 [1 ],OO0O0O0O0O0O0O0OO ),O000000O0OO0O0000 [0 ]))#line:319
		elif OOOOO00OOOOOOOOO0 [1 ]==O000000O0OO0O0000 [0 ]:#line:320
			O0OO0OOOOOO0000OO .append ((OOOOO00OOOOOOOOO0 [0 ],O000000O0OO0O0000 [1 ]+f15 (OOOOO00OOOOOOOOO0 [0 ],OOOOO00OOOOOOOOO0 [1 ]),f15 (OOOOO00OOOOOOOOO0 [0 ],OO0O0O0O0O0O0O0OO ),O000000O0OO0O0000 [0 ]))#line:321
	return O0OO0OOOOOO0000OO #line:322
def f25 (OOOOOOO0000O00OO0 ,OO00OOOO00O000O00 ):#line:326
	#if OOOOOOO0000O00OO0 .getPath ()is not None :#line:328
	#	OOOOOO0O0OO0O00O0 =OOOOOOO0000O00OO0 .world .getGates ()#line:329
	#	O0000O0000000O000 =OOOOOOO0000O00OO0 .agent .getLocation ()#line:330
	#	for OO000O00O00000O00 in OOOOOOO0000O00OO0 .getPath ()+[OOOOOOO0000O00OO0 .getDestination ()]:#line:331
	#		if O0000O0000000O000 is not None :#line:332
	#			O000OOO0O00000OOO =f13 (O0000O0000000O000 ,OO000O00O00000O00 ,OOOOOO0O0OO0O00O0 )#line:333
	#			if O000OOO0O00000OOO is not None :#line:334
	#				OOOOOOO0000O00OO0 .setPath (None )#line:336
	#				OOOOOOO0000O00OO0 .agent .stopMoving ()#line:337
	#				return None #line:338
	#		O0000O0000000O000 =OO000O00O00000O00 #line:339
		return None #line:341
def f26 (O00O0O0OOOO000O00 ):#line:346
	return None #line:350
def f14 (O000000OOO0O00O00 ):#line:357
	if O000000OOO0O00O00 .path !=None and O000000OOO0O00O00 .agent .moveTarget !=O000000OOO0O00O00 .destination :#line:358
		OO0O0000000O0O000 =f13 (O000000OOO0O00O00 .agent .rect .center ,O000000OOO0O00O00 .destination ,O000000OOO0O00O00 .world .getLines ())#line:359
		if OO0O0000000O0O000 ==None :#line:360
			OOOOOO0O0OO000O00 =False #line:361
			for O0OO00OO0O000OOOO in O000000OOO0O00O00 .world .getPoints ():#line:362
				if f12 ((O000000OOO0O00O00 .agent .rect .center ,O000000OOO0O00O00 .destination ),O0OO00OO0O000OOOO )<O000000OOO0O00O00 .agent .getRadius ()*2.0 :#line:363
					OOOOOO0O0OO000O00 =True #line:364
			if not OOOOOO0O0OO000O00 :#line:365
				return True #line:366
	return False #line:367
def f27 (OO0000O0O0OOOOO0O ,O00OO0O0O00O0OO00 ,OOOO000OO000OO00O ,OO0OO000OOO0O0OOO ,OOOO0O00OO0000OO0 ):#line:374
	OOOO000OO000OO00O =copy .deepcopy (OOOO000OO000OO00O )#line:375
	#OO000O0OOO0000OOO =OO0OO000OOO0O0OOO .getLines ()#line:377
	#O0O0O000OOO0OOOOO =None #line:378
	#OOO0O0OOOO0OOOO00 =None #line:379
	#for O0OOO0O0O0000OO0O in OOOO000OO000OO00O :#line:380
	#	OO000O0O0O0000O0O =f13 (OO0000O0O0OOOOO0O ,O0OOO0O0O0000OO0O ,OO000O0OOO0000OOO )#line:381
	#	if OO000O0O0O0000O0O ==None :#line:382
	#		OOO0OOO0O00OOO0OO =False #line:383
	#		for OOO0OO00O000OO000 in OO0OO000OOO0O0OOO .getPoints ():#line:384
	#			if f12 ((OO0000O0O0OOOOO0O ,O0OOO0O0O0000OO0O ),OOO0OO00O000OO000 )<OO0OO000OOO0O0OOO .agent .getRadius ()*2.0 :#line:385
	#				OOO0OOO0O00OOO0OO =True #line:386
	#		if not OOO0OOO0O00OOO0OO :#line:387
	#			O0O0O000OOO0OOOOO =O0OOO0O0O0000OO0O #line:388
	#	if OOO0O0OOOO0OOOO00 ==None :#line:389
	#		O0OOOOO00000O0O0O =f13 (O0OOO0O0O0000OO0O ,O00OO0O0O00O0OO00 ,OO000O0OOO0000OOO )#line:390
	#		if O0OOOOO00000O0O0O ==None :#line:391
	#			OOO0OOO0O00OOO0OO =False #line:392
	#			for OOO0OO00O000OO000 in OO0OO000OOO0O0OOO .getPoints ():#line:393
	#				if f12 ((O00OO0O0O00O0OO00 ,O0OOO0O0O0000OO0O ),OOO0OO00O000OO000 )<OO0OO000OOO0O0OOO .agent .getRadius ()*2.0 :#line:394
	#					OOO0OOO0O00OOO0OO =True #line:395
	#			if not OOO0OOO0O00OOO0OO :#line:396
	#				OOO0O0OOOO0OOOO00 =O0OOO0O0O0000OO0O #line:397
	#O00O0O0OO000O0O00 =[]#line:398
	#O0OO0OO0OOO0O0O0O =False #line:399
	#O0O0O00OO0OO000O0 =False #line:400
	#for O0OOO0O0O0000OO0O in OOOO000OO000OO00O :#line:401
	#	if O0O0O00OO0OO000O0 ==False :#line:402
	#		if O0OO0OO0OOO0O0O0O ==False :#line:403
	#			if O0OOO0O0O0000OO0O ==O0O0O000OOO0OOOOO :#line:404
	#				O00O0O0OO000O0O00 .append (O0OOO0O0O0000OO0O )#line:405
	#				O0OO0OO0OOO0O0O0O =True #line:406
	#		else :#line:407
	#			O00O0O0OO000O0O00 .append (O0OOO0O0O0000OO0O )#line:408
	#		if O0OOO0O0O0000OO0O ==OOO0O0OOOO0OOOO00 :#line:409
	#			O00O0O0OO000O0O00 .append (O0OOO0O0O0000OO0O )#line:410
	#			O0O0O00OO0OO000O0 =True #line:411
	#OOOO000OO000OO00O =O00O0O0OO000O0O00 #line:412
	return OOOO000OO000OO00O #line:414
def f24 (O00O000O0OO00OO00 ):#line:421
	#if O00O000O0OO00OO00 .path !=None and O00O000O0OO00OO00 .agent .moveTarget !=O00O000O0OO00OO00 .destination :#line:423
	#	if f14 (O00O000O0OO00OO00 ):#line:424
	#		O00O000O0OO00OO00 .path =[]#line:425
	#		O00O000O0OO00OO00 .agent .moveToTarget (O00O000O0OO00OO00 .destination )#line:426
	#		return True #line:427
	#	elif f11 (O00O000O0OO00OO00 ):#line:428
	#		O00O0O0O0O0O0OOO0 =O00O000O0OO00OO00 .path .pop (0 )#line:429
	#		O00O000O0OO00OO00 .agent .moveToTarget (O00O0O0O0O0O0OOO0 )#line:430
	#		return True #line:431
	return False #line:433
def f11 (O00O0OOOOOO00O000 ):#line:439
	if O00O0OOOOOO00O000 .path !=None and len (O00O0OOOOOO00O000 .path )>0 :#line:440
		O0OO00OOOO00O00OO =O00O0OOOOOO00O000 .path [0 ]#line:441
		OOO00OOO000O0000O =f13 (O00O0OOOOOO00O000 .agent .rect .center ,O0OO00OOOO00O00OO ,O00O0OOOOOO00O000 .world .getLines ())#line:442
		if OOO00OOO000O0000O ==None :#line:443
			OO000O00O0OO0OO00 =False #line:444
			for O0OO00O00O0000O0O in O00O0OOOOOO00O000 .world .getPoints ():#line:445
				if f12 ((O00O0OOOOOO00O000 .agent .rect .center ,O0OO00OOOO00O00OO ),O0OO00O00O0000O0O )<O00O0OOOOOO00O000 .agent .getRadius ()*2.0 :#line:446
					OO000O00O0OO0OO00 =True #line:447
			if OO000O00O0OO0OO00 :#line:448
				return False #line:449
			else :#line:450
				return True #line:451
	return False #line:452