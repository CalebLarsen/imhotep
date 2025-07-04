10 REM IMHOTEP - PYRAMID BUILDER * VERSION 2.5
20 REM COPYRIGHT (C) 1980 TERRY CLARK COLUMBUS IN

Clear space, set graphic mode, and darw introductory picture.

30 TEXT : HOME : GR : GOSUB 1200 : NN = 0

Initialize the contents of some variables

50 READ B$:P = 300000:D = 2500:S = 330 : T = 0 : W = 0 : ER = 0 : N = 0: IM$ = "IMHOTEP"

Clear screen and print introductory pages.

60 TEXT : HOME : GOSUB 61 : GOTO 70

61 PRINT TAB(20)"*": PRINT TAB(19)"***": PRINT TAB(18)"*****" : PRINT TAB(17)"*******": PRINT TAB(16)"*********": PRINT : PRINT : RETURN

70 PRINT TAB(17)"IMHOTEP": PRINT TAB(13)"PYRAMID BUILDER": PRINT : PRINT
75 PRINT "WRITTEN BY: TERRY CLARK": PRINT "TRANSLATED TO APPLE BY: M.P. ANTONOVICH": PRINT : PRINT: GOSUB 61

80 FOR I2 = 1 TO 5000: NEXT I2: HOME

85 PRINT "++++A DECREE FROM ZOSER,": PRINT "    THE GOLDEN HORUS,": PRINT "    BULL OF KHEM.++++"
90 PRINT : PRINT "TO IMHOTEP, MASTER MASON:"
100 PRINT "IMHOTEP, THE PHAROAH HAS COMMANDED A","PYRAMID TO BE BUILT.  THE HORUS DESIRES","THIS GLORY TO HIS NAME TO BE FINISHED","WITHIN A PERIOD OF TWELVE YEARS."
130 PRINT "YOUR OBVERSEER IS ";B$: PRINT "HE IS TO OBEY YOUR COMMANDS.": PRINT : PRINT
140 PRINT "HIT ANY KEY TO CONTINUE ";: GET A$

Jump to the pyramid drawing routine for an initial pyramid.

141 HOME
142 IF T = 0 THEN 163
145 GOSUB 690

A report on the current state of affairs is printed under a separate page.

150 VTAB 21: PRINT "WORK SITE AFTER ";T;"YEARS."

161 GOSUB 162: GOTO 163
162 FOR I1 = 1 TO 5000: NEXT I1: RETURN
163 TEXT : HOME
164 PRINT "POPULATION OF KHEMI - "; INT(P)
165 PRINT "PHAROAH OWNS "; INT (S);" GRAIN STOREHOUSES.": PRINT "NILE FLOODED "; INT (D);" TELS OF LAND."
180 PRINT : PRINT "# OF PEOPLE YOU WISH ON WORK FORCE": INPUT W
190 IF (W > P) OR (W < 0) THEN 780
200 PRINT : PRINT "FROM "; INT (S);" STOREHOUSES OWNEWD BY RA,"
210 INPUT "HOW MANY WILL FEED WORKERS ";I
220 IF (I > S) OR (I < 0) THEN 810
230 P = P - W:S = S - I

The desired actions are input and checked for legality

250 PRINT : PRINT "FROM "; INT(S);" REMAINING STOREHOUSES,"
260 PRINT "HOW MANY WILL FEED "; INT (P): INPUT "REMAINING PEOPLE ";J
270 IF (J> S) OR (J < 0) THEN 820
280 S = S - J
290 PRINT : PRINT "FROM "; INT(D);" TELS, HOW MANY DO YOU"
300 INPUT "WISH TO PLANT ";B
320 IF B > D OR B < 0 THEN 840
330 IF B > S * 100 THEN 870
340 IF B > P * 10 THEN 880

Screen is cleared.

350 TEXT : HOME : H = 0: GOSUB 61

The storehouses allotted to the workforce are used to determine the  number of people fed, at the ratio of one storehouse to 1000 people.  If feed too much, the number fed is the same as the total number of workers.

360 M = I * 1000: IF M - W > 0 THEN M = W

The same is done for the remainder of the population.  0 is used to determine how many people will move here, based on the quality of chow in Egypt.

370 L = J * 1000: R = L - P: IF R < 0 THEN R = 0
380 R = R + INT ( RND (1) * 1000 )
385 IF P - L > 0 THEN PRINT "YOU HAVE STARVED ";P - L;" PEOPLE.": ER = ER + 1
386 IF L - P > 0 THEN L = P

If you starve too many people, Zoser will get you.

390 IF P - L > P * .45 THEN 900

Various random elements are determined here.  The harvest and the number of storehouses gained, the chance of war, plague, and other catastrophic events are decided and the program jumps to the appropriate subroutines.  Time is advanced in line 470.

400 U = INT (RND(1) * 40): IF U < 4 THEN 1050
401 IF (M - W) < 0 THEN PRINT "YOU HAVE STARVED ";W-M;" WORKERS.":ER = ER + 2: GOTO 1050
410 Z = INT (RND (1) * 50): IF (Z < 9) AND (N > 4) THEN 1130
420 K = RND(1) * 3.5: S = S - (B / 100)
430 IF N > T * 2 THEN ER = ER - 1
440 IF ER > = 0 THEN O = INT( ((S * (RND(1)) + (ER * 4)) / 2)): IF O < 2 THEN S = S - O
450 IF ER < 0 THEN O = INT (S * (RND(1)) / 10): S = S + O
460 IF S < 0 THEN S = 0
470 S = S + ((B * K) / 10): T = T + 1
480 D = INT (RND(1) * 4000 + (O *.5)): Q = RND(1) * 30: IF Q > 22 THEN 950
481 IF (Q > 12) AND (Q < 18) THEN 1010
482 IF Q < 8 THEN 920
490 WA = RND (1) * 300: IF WQ < 19 THEN GOSUB 940
491 IF WA > 282 THEN GOSUB 1040
492 IF (WA < 210) AND (WA > 165) THEN GOSUB 960
493 IF (WA > 75) AND (WA < 130) THEN GOSUB 1020
494 IF (WA > 255) AND (WA < 260) THEN GOSUB 1030

The report of the year's progress is displayed, along with a statement on the mood of the Pharoah, if needed.

510 PRINT "THE HARVEST THIS YEAR WAS ";K / 10: PRINT "    STOREHOUSES PER TEL."
520 IF ER > = 0 THEN 530
521 IF (ER < 0) AND (O > 1) THEN PRINT "THE PRIESTS OF AMEN GAVE ZOSER,";O: PRINT "    STOREHOUSES OF GRAIN.":H = H + 1: GOTO 540
530 IF O < 2 THEN GOTO 540
531 IF ER > = 0 THEN PRINT O;" STOREHOUSES OF GRAIN WERE CLAIMED": PRINT "    BY THE PRIESTS OF AMEN.":H = H + 1
540 PRINT "THE POPULATION INCREASED BY ";R: PRINT "    PEOPLE."
550 P = R + L + M - U1 - V1
551 U1 = 0:V1 = 0
560 N = INT(N + (W - (W - M)) / 90000)
570 IF N > 20 THEN N = 20
580 IF (N < 21) AND (N > 0) THEN PRINT "THE WORK FORCE HAS COMPLETED ";N: PRINT "COURSES OF THE PYRAMID."
590 IF (N < 21) AND (D < 1000) AND (H < 10) THEN PRINT "THE VIZIERS PREDICT A POOR FLOOD NEXT","YEAR.":H = H + 2
591 IF (N < 21) AND (D > 3700) AND (H < 10) THEN PRINT "THE MELTING SNOW OF ETHIOP WELLS THE","NILE THIS SPRING.":H = H + 2
600 IF (N < 10) AND (T > 6) OR (ER > 3) AND (N < 20) THEN PRINT "PHAROAH IS BOTHERED BY YOUR INEFFICIENCY":H = H + 2
610 IF ER > 7 THEN PRINT "HE HAS DECREED, THAT FOR YOUR MISTAKES,","YOU WILL BE EXILED TO THE RED LAND OF","THE EAST.": GOTO 660
620 IF H < 2 THEN PRINT IM$;",": PRINT "AN UNEVENTFUL YEAR."
621 IF (H > 8) AND (H < 14) THEN PRINT IM$;",": PRINT "A VERY EVENTFUL YEAR."
624 PRINT "HIT ANY KEY TO CONTINUE ";: GET A$
625 IF T = 6 THEN GOSUB 1330
630 GOSUB 690
640 IF T > = 12 THEN 890
650 S = INT (S * 10 + .5) / 10: D = INT (D * 10 + .5) / 10: P = INT (P * 10 + .5) / 10: GOTO 150

End of program.

660 PRINT "IMHOTEP WILL YOU TRY AGAIN? (Y/N) ";: GET V$
661 IF V$ = "Y" THEN RUN
662 IF V$ = "N" THEN TEXT : HOME : END
670 GOTO 660


This subroutine is used to redraw the initial picture, and then draw the pyramid, course by course.

690 HOME : GR : GOSUB 1200: COLOR=13:E = 0:F = 39:Y = 39
691 IF N = 0 THEN RETURN
692 IF NN > 0 THEN FOR G = 1 TO NN: HLIN E,F AT Y: E = E + 1: F = F - 1: Y = Y -1: NEXT G
693 FOR G = NN + 1 TO N: FOR EE = E TO F
694 PLOT EE,Y: SD = PEEK ( -16336) + PEEK(-16336): FOR PA = 1 TO 50: NEXT PA: NEXT EE
695 E = E + 1: F = F -1: Y = Y - 1: NEXT G
696 NN = N
750 IF N = 20 THEN 970
760 RETURN

Here are the punishments for your errors, which are kept track of in the variable O.  O is used here to keep the screen from being filled to the point of over scrolling.

780 PRINT IM$;",": PRINT "ZOSER HEARD YOUR FOOLISHNESS.": PRINT "HE HAS EXILED ";B$;".": ER = ER + 1
790 ONERR GOTO 1190
800 READ B$: PRINT B$;" HAS BEEN ASSIGNED AS OVERSEER.": PRINT "NOW...": GOTO 180
810 PRINT IM$;",": PRITN "DO NOT JEST,": PRINT "THE HAWK'S EARS ARE SHARP.": ER = ER + 1: GOTO 200
820 PRINT IM$;",": PRINT "I, ";B$;", WARN YOU NOT": ER = ER + 1
830 PRINT "TO MOCK PHAROAH ZOSER. HIS FLAIL IS","SWIFT.": GOTO 250
840 PRINT IM$;",": PRINT "PHAROAH HAS KILLED ";B$: PRINT "YOUR OVERSEER.": ER = ER + 1
850 ONERR GOTO 1190
860 READ B$: PRINT "I AM ";B$;"YOUR NEW OVERSEER.": PRINT "NOW...": GOTO 290
870 PRINT "THERE IS ONLY ENOUGH GRAIN TO PLANT ";S*100-11: PRINT "TELS.": ER = ER + 1: IF S*100-1 < 0 THEN 901
871 GOTO 290
880 PRINT "THERE ARE ONLY ENOUGH PEOPLE TO PLANT": PRINT P * 10;"TELS.": ER = ER + 1: GOTO 290
890 PRINT "YOU HAVE RUN OUT OF TIME, ZOSER WANTS","YOUR HEAD.": GOTO 660
900 REM YOU KILLED TOO MANY PEOPLE
901 PRINT "ZOSER WANTS YOU MUMIFIED ALIVE IN THE ","HOUSE OF THE DEAD.": GOTO 660
920 Q = RND(1)*(P/2)*5: Q = INT(Q+.5): PRINT "A PESTILENCE DESCENDED FROM AMEN-RE.":H = H + 1
930 PRINT Q;" PEOPEL DIED.":V1 = Q: GOTO 510
940 Q = INT (RND(1) * P): PRINT "HYKSOS WITH CHARIOTS AND BLADES OF","BLACK EVIL METAL HAVE ATTACKED KHEM.";Q;" PEOPLE HAVE BEEN KILLED.":V1 = Q: H = H + 3: RETURN
950 V = INT (RND(1)*50): PRINT "NUBIAN EMISSARIES HAVE BROUGHT TRIBUTE","OF ";V;" STOREHOUSES OF GRAIN.": S = S + V: H = H + 2: GOTO 510
960 Q + INT ( RND(1) * P): PRINT "ACHEAN BARBARIANS FROM THE NORTHERN SEA","HAVE RAIDED THE DELTA ";Q: PRINT "PEOPLE HAVE BEEN KILLED.":V1 = Q: H = H + 3: RETURN

970 I2 = 2000
980 PRINT "IMHOTEP, YOU HAVE FULFILLED THE WISH": FOR I1 = 1 TO I2: NEXT I1
981 PRINT "OF PHAROAH.  YOUR REWARD IS THE GREAT": FOR I1 = 1 TO I2: NEXT I1
982 PRINT "BOON OF BEING ENTOMBED WITH YOUR LORD": FOR I1 = 1 TO I2: NEXT I1
983 PRINT "AND MASTER, ZOSER, THE GOLDEN HORUS.": FOR I1 = 1 TO I2: NEXT I1: GOTO 660

1010 V = INT (RND(1) * 50): PRINT "A MILITARY CAMPAIGN LED BY ZOSER HAS","BROUGHT AND ADDITIONAL ";V;" TELS": PRINT "OF LAND INTO THE DOUBLE-KINGDOM.": D = D + V: H = H + 3: GOTO 510

1020 V = INT(RND(1)*50 + 20): PRINT "MINOAN MERCHANTS HAVE BROUGHT ";V: PRINT "STOREHOUSES OF GRAIN TO TRADE FOR": PRINT "METHODS OF BUILDING AS PRACTICED IN","KHEMI.": S = S + V: H = H + 4: RETURN

1030 V = INT (RND(1) * 100): PRINT "THE PHAROAH'S NEW SYRIAN BRIDE BROUGHT","A DOWRY OF ";V;" STOREHOUSES": PRINT "OF GRAIN.": S = S + V: H = H + 3: RETURN

1040 V = INT (RND(1)*W): V1 = V: W = W - V: PRINT "A FANATICAL REBEL-PRIEST HAS ESCAPED","WITH ";V;" WORKERS INTO THE": PRINT "WILDERNESS OF THE SINAI.": H = H + 3: RETURN

1050 IF W = 0 THEN RETURN
1060 U = INT (RND(1)*100): PRINT "THE WORK FORCE HAS REBELLED. ";U
1070 PRINT "WORKERS, AND ";B$;", THE OVERSEER,": PRINT "WERE KILLED BY"
1080 PRINT "PHAROAH'S VICTORIOUS ANUBIS SQUADRON."
1090 U1 = U: W = W - U
1100 ONERR GOTO 1190
1110 READ B$: PRINT "THE GREAT ZOSER HAS CHOSEN ";B$: PRINT "TO BE YOUR NEW OVERSEER.":H = H + 6: GOTO 420
1130 Z = INT(RND(1) * 2 + 2): N = N - Z: W = W - INT(W * .25): M = W + P: IF NN > N THEN NN = N
1140 PRINT Z;" COURSES OF THE PYRAMID HAVE": PRINT "COLLAPSED AND ONE-FOURTH OF THE WORK","FORCE WAS LOST.": H = H + 3: GOTO 420
1160 N = 20: GOTO 690

Here are the overseers.

1180 DATA "MENE-PTAH","RA-ANX-TETA","ATUM-ATON","SETEP-EN-RE","RAMOSE","MERI-ATUM","KA-RES","MAATTUM","MERI-TEHU"
1181 DATA "TOTHMES","RE-MES-SES","PTAHMES","MERIPASHTU"

Store the picture for the introduction and annual picture.

CODE NOT COPIED HERE

1220 VTAB 21: PRINT TAB(16)"IMHOTEP"
1225 IF TZ = 1 THEN RETURN
1230 FOR ZZ = 0 TO 5000: NEXT ZZ: TZ = 1: RETURN

It is jubilee time.  Here Pharoah uses the number of mistakes made (ER), the degree of completion (N), the number of storehouses (S), and the number of people (P) to rate the ability of Imhotep.  If rewarded, Imhotep has his mistakes erased from his record, which, by the way, will get the priests off his back.

1330 TEXT : HOME : GOSUB 61 : PRINT TAB(16)"JUBILEE": PRINT "IT IS TIME FOR PHAROAH'S JUBILEE.","YOU HAVE USED HALF OF YOUR TIME."
1340 IF (N = 20) OR ((N > 10) AND (P > 300000) AND (S * 1000 > P) AND (ER < 2)) THEN PRINT IM$: PRINT "PHAROAH IS PLEASED WITH YOUR": PRINT "PERFORMANCE SO FAR AND BESTOWS A GREAT","HONOR ON YOU. FROM THIS MOMENT YOU ARE","KNOWN AS 'GREAT LORD IMHOTEP'."
1345 IF (N = 20) OR ((N > 10) AND (P > 300000) AND (S * 1000 > P) AND (ER < 2)) THEN ER = -1:IM$ = "GREAT LOAD IMHOTEP": GOTO 1370
1350 IF (N < 7) AND (ER > 3) AND (P < 300000) AND (S * 1000 < = P + 50) THEN PRINT IM$: PRINT "PHAROAH IS DISPLEASED WITH YOU AND","DESIRES FOR YOU TO SUFFER THE DISHONOR","OF BEARING THE TITLE 'IMHOTEP THE","INCOMPETENT'."
1355 IF (N < 7) AND (ER > 3) AND (P < 300000) AND (S * 1000 < = P + 50) THEN ER = ER + 1: IM$ = "IMHOTEP THE INCOMPETENT": GOTO 1370
1360 PRINT IM$: PRINT "PHAROAH FEELS YOU HAVE NOT PUT FORTH A","GOOD EFFORT AND DESIRES TO REMIND YOUR","OF YOUR RESPONSIBILITIES WITH THE","TITLE 'IMHOTEP-HORUS-WATCHES'.": IM$ = "IMHOTEP-HORUS-WATCHES"
1370 PRINT "HIT ANY KEY TO CONTINUE ";: GET A$: RETURN

