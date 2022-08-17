Search.setIndex({docnames:["additionalInfos/getPrivateKeyFromLightWallet","additionalInfos/index","additionalInfos/installDefichainNode","additionalInfos/mnemonicSeedForWallet","api/exceptions","api/node/accounts","api/node/blockchain","api/node/control","api/node/generating","api/node/index","api/node/loan","api/node/masternodes","api/node/mining","api/node/network","api/node/node","api/node/oracles","api/node/poolpair","api/node/rawtransactions","api/node/spv","api/node/tokens","api/node/util","api/node/vault","api/node/wallet","api/node/zmq","api/ocean/address","api/ocean/blocks","api/ocean/fee","api/ocean/index","api/ocean/loan","api/ocean/masternodes","api/ocean/ocean","api/ocean/oracles","api/ocean/poolpair","api/ocean/prices","api/ocean/rawTx","api/ocean/rpc","api/ocean/stats","api/ocean/tokens","api/ocean/transactions","index","instructions/progressAndUpdates","instructions/quickstart","instructions/rawMethodsOverview","legal/community","legal/licenseAndDisclaimer"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":5,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["additionalInfos/getPrivateKeyFromLightWallet.rst","additionalInfos/index.rst","additionalInfos/installDefichainNode.rst","additionalInfos/mnemonicSeedForWallet.rst","api/exceptions.rst","api/node/accounts.rst","api/node/blockchain.rst","api/node/control.rst","api/node/generating.rst","api/node/index.rst","api/node/loan.rst","api/node/masternodes.rst","api/node/mining.rst","api/node/network.rst","api/node/node.rst","api/node/oracles.rst","api/node/poolpair.rst","api/node/rawtransactions.rst","api/node/spv.rst","api/node/tokens.rst","api/node/util.rst","api/node/vault.rst","api/node/wallet.rst","api/node/zmq.rst","api/ocean/address.rst","api/ocean/blocks.rst","api/ocean/fee.rst","api/ocean/index.rst","api/ocean/loan.rst","api/ocean/masternodes.rst","api/ocean/ocean.rst","api/ocean/oracles.rst","api/ocean/poolpair.rst","api/ocean/prices.rst","api/ocean/rawTx.rst","api/ocean/rpc.rst","api/ocean/stats.rst","api/ocean/tokens.rst","api/ocean/transactions.rst","index.rst","instructions/progressAndUpdates.rst","instructions/quickstart.rst","instructions/rawMethodsOverview.rst","legal/community.rst","legal/licenseAndDisclaimer.rst"],objects:{"defichain.Node":[[14,1,1,"","decrypt_wallet"],[14,1,1,"","load_wallet"],[14,1,1,"","test_connection"]],"defichain.exceptions":[[4,0,1,"","BadMethod"],[4,0,1,"","BadRequest"],[4,0,1,"","Forbidden"],[4,0,1,"","InternalServerError"],[4,0,1,"","NotFound"],[4,0,1,"","ServiceUnavailable"],[4,0,1,"","Unauthorized"],[4,0,1,"","UnprocessableEntity"],[4,0,1,"","WrongParameters"]],"defichain.node":[[5,0,1,"","Accounts"],[6,0,1,"","Blockchain"],[7,0,1,"","Control"],[8,0,1,"","Generating"],[10,0,1,"","Loan"],[11,0,1,"","Masternodes"],[12,0,1,"","Mining"],[13,0,1,"","Network"],[15,0,1,"","Oracles"],[16,0,1,"","Poolpair"],[17,0,1,"","Rawtransactions"],[18,0,1,"","Spv"],[19,0,1,"","Tokens"],[20,0,1,"","Util"],[21,0,1,"","Vault"],[22,0,1,"","Wallet"],[23,0,1,"","Zmq"]],"defichain.node.Accounts":[[5,1,1,"","accounthistorycount"],[5,1,1,"","accounttoaccount"],[5,1,1,"","accounttoutxos"],[5,1,1,"","executesmartcontract"],[5,1,1,"","futureswap"],[5,1,1,"","getaccount"],[5,1,1,"","getaccounthistory"],[5,1,1,"","getburninfo"],[5,1,1,"","getpendingdusdswaps"],[5,1,1,"","getpendingfutureswaps"],[5,1,1,"","gettokenbalances"],[5,1,1,"","listaccounthistory"],[5,1,1,"","listaccounts"],[5,1,1,"","listburnhistory"],[5,1,1,"","listcommunitybalances"],[5,1,1,"","listpendingdusdswaps"],[5,1,1,"","listpendingfutureswaps"],[5,1,1,"","sendtokenstoaddress"],[5,1,1,"","sendutxosfrom"],[5,1,1,"","utxostoaccount"],[5,1,1,"","withdrawfutureswap"]],"defichain.node.Blockchain":[[6,1,1,"","clearmempool"],[6,1,1,"","getbestblockhash"],[6,1,1,"","getblock"],[6,1,1,"","getblockchaininfo"],[6,1,1,"","getblockcount"],[6,1,1,"","getblockfilter"],[6,1,1,"","getblockhash"],[6,1,1,"","getblockheader"],[6,1,1,"","getblockstats"],[6,1,1,"","getchaintips"],[6,1,1,"","getchaintxstats"],[6,1,1,"","getdifficulty"],[6,1,1,"","getgov"],[6,1,1,"","getmempoolancestors"],[6,1,1,"","getmempooldescendants"],[6,1,1,"","getmempoolentry"],[6,1,1,"","getmempoolinfo"],[6,1,1,"","getrawmempool"],[6,1,1,"","gettxout"],[6,1,1,"","gettxoutproof"],[6,1,1,"","gettxoutsetinfo"],[6,1,1,"","isappliedcustomtx"],[6,1,1,"","listgovs"],[6,1,1,"","listsmartcontracts"],[6,1,1,"","preciousblock"],[6,1,1,"","pruneblockchain"],[6,1,1,"","savemempool"],[6,1,1,"","scantxoutset"],[6,1,1,"","setgov"],[6,1,1,"","setgovheight"],[6,1,1,"","verifychain"],[6,1,1,"","verifytxoutproof"]],"defichain.node.Control":[[7,1,1,"","getmemoryinfo"],[7,1,1,"","getrpcinfo"],[7,1,1,"","help"],[7,1,1,"","logging"],[7,1,1,"","stop"],[7,1,1,"","uptime"]],"defichain.node.Generating":[[8,1,1,"","generatetoaddress"]],"defichain.ocean":[[24,0,1,"","Address"],[25,0,1,"","Blocks"],[26,0,1,"","Fee"],[28,0,1,"","Loan"],[29,0,1,"","Masternodes"],[31,0,1,"","Oracles"],[32,0,1,"","Poolpairs"],[33,0,1,"","Prices"],[34,0,1,"","RawTx"],[35,0,1,"","Rpc"],[36,0,1,"","Stats"],[37,0,1,"","Tokens"],[38,0,1,"","Transactions"]],defichain:[[14,0,1,"","Node"],[30,0,1,"","Ocean"],[4,2,0,"-","exceptions"]]},objnames:{"0":["py","class","Python class"],"1":["py","method","Python method"],"2":["py","module","Python module"]},objtypes:{"0":"py:class","1":"py:method","2":"py:module"},terms:{"0":[5,6,7,9,14,41],"0000":6,"00000000":6,"01":41,"0a454f39213285395e7420b1680378f46516b5389d7b4c42830795adb4487cd7":43,"1":[5,6,7,8,9,14,27,40,41],"10":[5,7,43],"100":5,"1000":[5,6],"103":5,"10th":6,"10th_percentile_feer":6,"11":8,"125h":43,"127":[9,14,41],"141":6,"157":6,"160":5,"1800":43,"1970":6,"1d00ffff":6,"1f3":6,"2":[5,6,7,9,27],"20":6,"2022":[0,44],"25":43,"250":43,"256":3,"25th":6,"25th_percentile_feer":6,"28":6,"3":[5,6,9,27],"30":[30,41,43],"3000000":6,"4":[6,41],"40000":43,"403":4,"45":43,"5":5,"50":43,"50th":6,"50th_percentile_feer":6,"6":6,"60":14,"6250":43,"7500":43,"75th":6,"75th_percentile_feer":6,"8":6,"8554":[9,14,41],"86400":6,"9":40,"90th":6,"90th_percentile_feer":6,"\u00f6kosystem":43,"\u00fcbernommen":43,"au\u00dfer":43,"boolean":6,"byte":[6,7],"case":6,"class":[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38],"default":[3,5,6,14],"do":[3,30,44],"erm\u00f6glicht":43,"f\u00fcr":43,"final":[6,42],"float":6,"function":[0,6,9,27,43],"funktionalit\u00e4t":43,"gro\u00dfteil":43,"hinzuf\u00fcgen":43,"import":[9,14,27,30,41],"int":[5,6,7,8,14],"m\u00f6glich":43,"new":43,"public":[6,43],"return":[5,6,7,8,14,30,41],"true":[3,5,6,7],"try":[3,8],"ver\u00f6ffentlichung":43,"verst\u00e4ndlich":43,"vorschlagsgeb\u00fchr":43,"while":[0,3],"zuk\u00fcnftig":43,A:[0,4,6,7,44],AND:44,AS:[0,3,44],As:0,BE:44,BUT:44,Be:3,But:[0,3],By:[0,6,39,44],FOR:44,For:[6,9,27,39,41,43],IN:44,IS:[0,3,44],If:[4,5,6,7,9,14,27,30,39,43],In:[0,1,2,6,7,39,40,43],Is:6,It:[5,6,9],NO:44,NOT:44,Not:[6,40],OF:[0,3,44],OR:44,One:6,THE:[0,3,44],TO:44,The:[4,5,6,7,8,9,14,27,30,41,42,44],These:9,To:[3,6,43],WITH:44,Will:27,With:3,_from:5,abandontransact:42,abfrag:43,abgebildet:43,abl:[0,3],abort:6,abortrescan:42,about:[5,6,7,9,27,40,43],abov:[6,7,44],absolut:42,acceler:43,accept:6,access:0,account:[9,40,42],accountchang:7,accounthistorycount:[5,42],accounttoaccount:[5,42],accounttoutxo:[5,42],acindex:5,across:6,action:[4,6,42,44],activ:[6,7],activate_after_block:42,activateafterblock:42,active_command:7,actual:[6,9,27],ad:43,add:7,addit:[7,40,43],addition:3,addmultisigaddress:42,addnod:42,addpoolliquid:42,addr:6,address1:5,address2:5,address:[5,6,8,27,40,42,43],address_filt:42,address_typ:42,addrman:7,affect:[0,6],after:14,again:14,ago:43,agre:[39,44],algorithm:43,algorithmu:43,all:[3,5,6,7,9,27,39,40,42,43,44],alloc:7,allow:43,almost:0,alreadi:[14,43],also:[0,3,30,39,40],alwai:[0,3,6],amount1:9,amount2:9,amount:[5,6,7,42,43],amountfrom:42,an:[0,3,4,5,6,7,9,30,39,41,42,43,44],analysieren:43,analyz:43,analyzepsbt:42,ancestor:6,ancestorcount:6,ancestorfe:6,ancestors:6,anchor:7,anforder:43,angefragt:43,ani:[0,3,6,43,44],ansteuern:43,anwendungen:43,anyth:30,api:39,appar:4,appear:6,appli:6,applic:43,appointoracl:42,approach:3,ar:[3,5,6,7,8,9,14,27,41,42],arbeiten:43,arena:7,argument:[5,7,9],aris:44,arrai:[5,6,7,8,9],ascend:5,asm:6,asset:[0,3],assign:[9,27],associ:44,assum:6,attack:0,attr:6,attribut:6,auch:43,auf:43,aufruf:43,aufzurufen:43,authent:4,author:44,autom:0,automat:[6,9],automatic_prun:6,autoselect:5,avail:[4,5,6,7,39,42],averag:6,avgfe:6,avgfeer:6,avgtxsiz:6,avoid_reus:[3,42],back:5,background:43,backup:3,backupwallet:42,badmethod:4,badrequest:4,balanc:[3,5,6],balance_typ:5,bantim:42,base58:5,base:[0,6,43],basic:[6,9,27],basiert:43,bear:43,becaus:[0,6,43],bech32:5,becom:14,been:[0,4,7,43],befehl:43,befindlichen:43,befor:[3,6,8,14],begin:6,being:7,belong:[5,9],below:[6,9,27],bench:7,benutz:43,berechnen:43,beschleunigt:43,besitzt:43,best:[6,43],bestblock:6,bestblockhash:6,bestimmten:43,bietet:43,bip125:6,bip32deriv:42,bip70:6,bip9:6,bip:6,bisher:43,bit:6,blank:42,block:[5,6,8,14,27,30,40,41,43],blockchain:[3,9,14,39,40,41,42,43],blockcount:[14,42,43],blockhash:[6,42],blockhead:6,blockheight:[5,6,42],bogos:6,bool:[5,6,7,42],bot:43,both:7,bound:[39,44],branch:6,branchlen:6,broadcast:[5,6],btc:[5,9,41,43],bumpfe:42,buri:6,burn:5,burnt:5,c:44,calcul:[0,3,43],call:[4,6,7,8,39],can:[0,2,3,6,9,14,27,30,39,40,41,43],cannot:4,care:[9,27,43],categori:7,certain:6,chain:[5,6,42],chainfrom:42,chainstat:6,chaintip:5,chainto:42,chainwork:6,chang:[3,5,6,30,42],charg:44,check:[6,39,41],checklevel:[6,42],child:6,choos:3,chunk:7,chunks_fre:7,chunks_us:7,circa:43,claim:44,clear:[3,6],clearban:42,clearmempool:[6,42],cli:[0,43],client:4,clone:41,close:42,closevault:42,cmpctblock:7,code:[3,6,39,41],coin:5,coinbas:[5,6],coindb:7,collateraladdress:42,collateralamount:42,com:[30,41],combinepsbt:42,combinerawtransact:42,combo:6,command:[0,6,7,39,41,42,43],comment:42,comment_to:42,commiss:42,commit:6,commun:[0,5,14,30,40],compil:7,complet:[2,6,7],compositeswap:[9,41,42,43],compromis:0,comput:6,concentr:43,condit:[4,44],conf:14,conf_target:42,configur:[7,43],confirm:6,connect:[0,6,9,14,27,30,39,40,41,44],consid:6,consist:[9,27],contain:[4,5,6,7],content:6,contract:[5,6,44],control:[9,27,40,42],converttopsbt:42,copi:44,copyright:44,corner:[9,27],correct:5,correspond:6,could:[3,4,6,7],count:[5,6,42],creat:[5,9,27,30,41,43],createloanschem:42,createmasternod:42,createmultisig:42,createpoolpair:42,createpsbt:42,createrawtransact:42,createtoken:42,createvault:42,createwallet:[3,42],creation:43,crumb:5,crypto:3,cscript:5,currenc:42,current:[6,7,43],custom:6,customreward:42,customtxtyp:5,daemon:7,damag:44,dat:1,data:[4,6,7,27,39,41,42,43],databas:[6,43],date:40,daten:43,datenbank:43,db:[5,7],dbtcdfiswap:5,dctkz5sqrqf4vgvsgra76ptxenbcxprenp:9,de:[40,43],deal:44,dear:43,debug:[6,7],decentr:43,decim:42,decodecustomtx:42,decodepsbt:42,decoderawtransact:42,decodescript:42,decreas:6,decrypt:[9,14],decrypt_wallet:14,defi:[5,6,7,9,14],defichain:[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40],defichainpython:41,defid:6,defin:6,delta:6,dem:43,denn:43,depend:6,deploy:6,deposittovault:42,deprec:6,deprecatedrpc:6,depth:[5,42],deriveaddress:42,desc:[6,42],descend:[5,6],descendantcount:6,descendantfe:6,descendants:6,describ:7,descriptor:[6,42],design:0,destin:[5,42],destinationaddress:42,destroyloanschem:42,detail:[6,7],determin:7,deutschland:43,develop:1,devic:[0,3],dezentralisierung:43,df1qdx0mllcvvrdfcrstyvp2pu4szp2pct5njcgwev:43,df1qzkf582h0sgfksj0yn0wxz0r9amyqfferm5wyc:9,dfchtlctx:42,dfi:[5,6,8,9,41],di:43,die:43,dieser:43,differ:[6,43],difficult:3,difficulti:6,directli:43,direkt:43,disable_private_kei:[3,42],disconnectnod:42,discontinu:0,discount:6,discret:6,discuss:43,disk:[6,7],disk_siz:6,diskussionsthread:43,distribut:44,divid:6,doc:[6,40],document:[0,6,39,40,43,44],doe:6,dokument:43,don:[3,39],down:[3,5],download:[0,6,43],downto:5,drive:43,dstaddress1:5,dtoken:[5,42],due:[4,6],dummi:42,dump:6,dumpprivkei:42,dumpwallet:42,durat:7,durch:43,dusd:5,each:[6,39],earlier:6,easi:43,ecosystem:43,effect:6,eg:6,ein:43,einem:43,einen:43,einer:43,einfach:43,einfachen:43,einstieg:43,einstiegspunkt:43,either:[5,6],elaps:[6,14],element:6,email:[39,43],emissionburn:5,empfangsadress:43,empti:[3,5,6,9],enabl:6,encod:[5,6],encount:4,encrypt:3,encryptwallet:42,end:[0,6,7],enforc:6,english:3,enough:6,ensur:43,enter:[6,14],entri:[6,43],entwicklern:43,entwicklung:43,entwicklungszeit:43,epoch:6,equal:6,eric:[41,43],error:[0,4],erstellen:43,es:43,estim:6,estimate_mod:42,estimatecollater:42,estimatefe:7,estimateloan:42,estimatesmartfe:42,estimatevault:42,eth:[5,9,41],evalu:7,even:[7,43],event:44,everi:[0,3,6,43],everyon:0,everyth:[3,43],exact:6,exampl:[5,6,7,8,9,14,27,30,41],except:[14,40,43],exclud:[6,7],exclude_categori:[7,42],exclude_custom_tx:42,execut:[5,6,9,27,41],executesmartcontract:[5,42],exist:[0,3,4],expect:[3,4,5,6],experiment:6,expiri:42,explan:[3,9,27],explicitli:6,explor:6,express:44,extract:[0,3,42],factor:[6,42],fail:[4,6,7],fals:[3,5,6,7],far:43,featur:6,fee:[5,6,27,40,43],fee_delta:42,feeburn:5,feerat:[6,42],feerate_percentil:6,fetch:6,few:[39,43],ffa579106ef8d396223c616b9a77b8dab22656648b55965fc9e541e864f0f9fd:6,field:[5,6],file:[1,6,7,44],filenam:42,filesystem:14,filter:[5,6],filtertyp:[6,42],finalizepsbt:42,find:[3,9,27],finish:[2,40,43],first:[5,6,43],fit:44,fix:6,fixedintervalpriceid:42,flag:[5,42],follow:[0,4,5,6,7,9,27,40,43,44],forbidden:4,fork:6,form:4,format:[5,6,9,42],fort:40,forward:5,found:[4,6,9,14,27],free:[7,44],from:[0,2,5,6,7,9,14,27,30,39,41,42,43,44],from_address:5,from_mnemon:3,fromaddress:41,full:[5,43],fulli:[3,6,43],fund:[0,5,39],fundrawtransact:42,funktion:43,funktionen:43,furnish:44,further:43,furthermor:43,futur:[4,5,6],futureswap:[5,7,42],gain:6,ganz:43,gegeben:43,gener:[4,6,7,9,40,42],generate_mnemon:3,generatetoaddress:[8,42],genesi:[5,6],germani:43,get:[1,2,5,7,9,27,39,41,43],getaccount:[5,42],getaccounthistori:[5,42],getactivemasternodecount:42,getaddednodeinfo:42,getaddressesbylabel:42,getaddressinfo:42,getanchorteam:42,getbal:42,getbestblockhash:[6,42],getblock:[6,42],getblockchaininfo:[6,42],getblockcount:[6,7,9,14,41,42],getblockfilt:[6,42],getblockhash:[6,42],getblockhead:[6,42],getblockstat:[6,42],getblocktempl:42,getburninfo:[5,42],getchaintip:[6,42],getchaintxstat:[6,42],getcollateraltoken:42,getconnectioncount:42,getcustomtx:42,getdescriptorinfo:42,getdifficulti:[6,42],getdusdswapblock:42,getfixedintervalpric:42,getfutureswapblock:42,getgov:[6,42],getinterest:42,getloaninfo:42,getloanschem:42,getloantoken:42,getmasternod:42,getmasternodeblock:42,getmemoryinfo:[7,42],getmempoolancestor:[6,42],getmempooldescend:[6,42],getmempoolentri:[6,42],getmempoolinfo:[6,42],getmininginfo:42,getmintinginfo:42,getnettot:42,getnetworkhashp:42,getnetworkinfo:42,getnewaddress:42,getnodeaddress:42,getoracledata:42,getpeerinfo:42,getpendingdusdswap:[5,42],getpendingfutureswap:[5,42],getpoolpair:42,getpric:42,getrawchangeaddress:42,getrawmempool:[6,42],getrawtransact:[6,42],getreceivedbyaddress:42,getreceivedbylabel:42,getrpcinfo:[7,42],getrpcstat:42,gettoken:42,gettokenbal:[5,42],gettransact:42,gettxout:[6,42],gettxoutproof:[6,42],gettxoutsetinfo:[6,42],getunconfirmedbal:42,getvault:42,getversioninfo:42,getwalletinfo:42,getzmqnotif:42,git:41,github:[41,43],give:[0,3],given:[4,6,14,43],glibc:7,gmt:6,go:3,good:3,gov:6,govern:6,grant:44,group:0,grundlag:43,guid:[2,43],h:6,ha:[3,4,6,7,40],handl:4,harden:6,hash:[5,6,8,42],hash_or_height:[6,42],hash_serialized_2:6,have:[3,5,6,27,39,43],hd:6,hdwallet:3,header:6,heap:7,height:[5,6,14,41,42],help:[7,9,42],here:[3,9,14,27,39,41],herebi:44,herunterladbar:43,hex:[5,6,9,42],hexadecim:6,hexdata:42,hexstr:42,hi:0,hierdurch:43,hint:6,hintergrund:43,histori:5,holder:44,hour:6,hourli:43,how:[1,6,8,39,41],htlcscriptaddress:42,http:[7,14,30,41],i:[0,3,9,27,43],icx_claimdfchtlc:42,icx_closeoff:42,icx_closeord:42,icx_createord:42,icx_getord:42,icx_listhtlc:42,icx_listord:42,icx_makeoff:42,icx_submitdfchtlc:42,icx_submitexthtlc:42,icx_takerfee_per_btc:6,icxorderbook:42,id:[5,6,9,42],idea:[39,43],ie:6,ignor:7,im:43,immedi:8,implement:[40,43],impli:44,importaddress:42,importmulti:42,importprivkei:[0,42],importprunedfund:42,importpubkei:42,importwallet:42,improv:[39,43],inact:7,includ:[5,6,7,44],include_categori:[7,42],include_empti:42,include_mempool:[6,42],include_remov:42,include_unsaf:42,include_watchonli:42,including_start:[5,42],increas:6,index:[6,42],indexed_amount:[5,42],indic:[5,6,7],individu:[9,27,41,43],individuel:43,info:6,inform:[2,5,6,7,9,27,40,41],initi:6,initialblockdownload:6,input:[5,6],ins:6,insid:3,instal:[1,3,39,40,43],instanc:30,instruct:[0,3],interact:[14,30],interest:42,interestr:42,interfac:[14,30],internalservererror:4,internet:[0,39],introc:[39,43,44],invalid:[3,6],ip:14,is_mine_onli:[5,42],isappliedcustomtx:[6,42],isdat:42,issu:[39,43],ist:43,iswit:42,item:7,iter:[5,8],its:[6,7],jan:6,javascript:43,jedem:43,jeden:43,jellyfish:43,joinpsbt:42,json:[5,6,7],just:[3,5,39,41],kann:43,kb:6,keep:[0,3,9,27],kei:[1,5,6,7,9,42],keypoolrefil:42,kind:[0,3,7,44],know:[0,40,43],known:6,konzentrieren:43,label:42,languag:[3,43],larg:43,last:[5,6],later:6,latest:[14,30,41],latter:6,least:6,left:[6,9,27],length:6,letter:5,level:7,leveldb:7,lexicograph:5,liabil:44,liabl:44,libev:7,librari:41,light:[1,3],lightwallet:30,like:[0,3],limit:[5,42,44],line:[3,6,39],link:39,liquid:43,list:[5,6,7,27,30,41],listaccount:[5,42],listaccounthistori:[5,42],listaddressgroup:42,listanchor:42,listauct:42,listauctionhistori:42,listban:42,listburnhistori:[5,42],listcollateraltoken:42,listcommunitybal:[5,42],listfixedintervalpric:42,listgov:[6,42],listlabel:42,listlatestrawpric:42,listloanschem:42,listloantoken:42,listlockunsp:42,listmasternod:42,listoracl:42,listpendingdusdswap:[5,42],listpendingfutureswap:[5,42],listpoolpair:42,listpoolshar:42,listpric:42,listreceivedbyaddress:42,listreceivedbylabel:42,listrpcstat:42,listsinceblock:42,listsmartcontract:[6,42],listtoken:42,listtransact:42,listunsp:42,listvault:42,listvaulthistori:42,listwallet:42,listwalletdir:42,live:6,load:[6,14],load_wallet:14,loadwallet:42,loan:[7,9,27,40,42],loan_liquidation_penalti:6,loanamount:42,loanschemeid:42,local:[5,6],localhost:14,locat:[0,9,14,27],lock:[6,7,14],locked_in:6,locktim:42,lockunsp:42,log:[7,42],logpath:7,look:[6,9],low:7,lowest:6,lp_daily_dfi_reward:6,lp_daily_loan_token_reward:6,lp_loan_token_split:6,lp_split:6,made:[3,9,27,43],mai:[4,5,6,9],main:[6,9,14,27,30],mainnet:30,maintain:6,make:[0,3,6],malloc:7,mallocinfo:7,manag:7,mani:8,manual:6,manuali:5,map:43,mark:6,market:43,masternod:[9,27,40,42],match:[0,6,9],maxblockheight:[5,42],maxbtcheight:42,maxconf:42,maxfe:6,maxfeer:[6,42],maxim:5,maximum:[5,6],maxmempool:6,maxpric:42,maxtri:[8,42],maxtxsiz:6,md:6,me:[39,43],mean:[5,6,7],meaningless:6,meantim:2,median:6,medianfe:6,mediantim:6,mediantxs:6,meist:43,memori:[6,7],mempool:[6,7],mempoolminfe:6,mempoolrej:7,meng:43,merchant:44,merg:44,merkl:6,merkleroot:6,messag:[4,42],metadata:6,method:[0,4,7,9,27,39,40,43],metric:6,microsecond:7,min:43,minbtcheight:42,mincolratio:42,minconf:42,mine:[5,6,8,9,40,42],minfe:6,minfeer:6,minim:5,minimum:6,minrelaytxfe:6,mintabl:42,minttoken:42,mintxsiz:6,mit:[39,43,44],mn_id:42,mnemon:1,mode:[5,6,7,42],modifi:[6,44],modifiedfe:6,modul:40,monei:43,more:[4,6,9,27,41,43],most:[6,9,27,43],msg:4,multi:6,multipl:[6,9],multisig:6,must:6,mxxa2sqmetjfbxcnbnbuzesbctn1jshxst:5,my:3,myaddress:8,mywallet:14,n:[5,6,9,42],name:[3,5,6,7,14,42],nblock:[6,8,42],neat:43,neccessari:5,need:[0,3,6,14,39,41],net:7,network:[5,6,9,30,40,42],neuen:43,neuer:43,never:6,newkeypool:[3,42],newli:8,newpassphras:42,newsiz:42,next:[0,6,43],nextblockhash:6,nnn:6,nnnnnnnn:[5,6],no_reward:[5,42],node:[1,3,5,6,7,8,10,11,12,13,15,16,17,18,19,20,21,22,23,39,42,43],nodeid:42,non:[5,6],nonc:6,none:[5,6,7,14],noninfring:44,nonutxo:6,normal:3,notat:6,note:6,notfound:4,noth:3,notic:44,notwendig:43,now:[0,3,43],nrequir:42,ntx:6,number:[5,6,7,9],numer:[6,7,9],obj:[5,42],object:[5,6,7,9,14,27,30],obtain:44,ocaen:30,occur:14,oceab:40,ocean:[24,25,26,28,29,31,32,33,34,35,36,37,38,39,40],oder:43,off:0,offer:[9,43],offertx:42,offlin:3,often:9,older:6,oldpassphras:42,onc:5,one:[0,3,6,9,39,41,43],ones:9,onli:[0,6,7,9,27,30,41],op_return:6,open:[39,43],oper:30,operatoraddress:42,optin:7,option:[5,6,7,8,9,14,30,42],oracl:[7,9,27,40,42],oracle_block_interv:6,oracle_devi:6,oracleid:42,ordentlich:43,order:[5,7],orderpric:42,ordertx:42,orphan:6,other:[3,6,7,9,39,43,44],otherwis:[5,44],out:[5,6,39,44],output:[5,6,9,27,42,43],overrid:6,overview:[9,40],own:5,owner:[5,42],owneraddress:42,ownerpubkei:42,p2pk:6,p2pkh:6,p2sh:[6,42],p2wpkh:6,packag:[3,43],page:[7,9,27,40],pairsymbol:42,paper:[0,3],param:5,paramet:[3,5,6,7,8,14,30],paremet:4,parent:6,part:[6,43],particular:[6,44],pass:[4,6],passphras:[3,42],password:[9,14,41,43],passwort:43,past:6,path:[6,7,14,42],paybackloan:42,pen:0,pend:[5,6],peopl:43,per:[6,43],percentil:6,perform:[9,27],period:6,permiss:44,permit:44,permitsigdata:42,person:[3,44],phase:[0,3],phrase:1,pick:5,pie:5,piec:[0,3],ping:[14,42],pip:[3,41,43],pkh:6,place:[0,3],placeauctionbid:42,plot:6,plu:0,point:[6,7,43],pool:[6,41,42,43],poolpair:[9,27,40,41,42,43],poolswap:42,port:[14,43],portion:44,posit:5,possibl:[3,6,9,43],potenti:6,preciou:6,preciousblock:[6,42],prefix:[6,42],prei:43,present:6,previou:[5,6],previous:[9,27],previousblockhash:6,price:[27,40,43],print:[14,30,43],prioriti:6,prioritisetransact:42,privat:1,privatekei:42,privkei:42,pro:43,process:[4,6],produc:6,product:40,program:43,programm:43,programmier:43,programmiersprach:43,programmiersprachen:43,progress:[6,9,27,43],project:[0,39,40],proof:[6,42],propos:43,protect:9,protocol:[14,30],provid:[0,3,4,6,43,44],proxi:7,prune:[6,7],prune_target_s:6,pruneblockchain:[6,42],pruneheight:6,psbt:42,pubkei:[6,42],pubkeyhash:6,publish:[40,41,43,44],pull:43,purpos:[42,44],put:[0,3],pypi:[41,43],python3:3,python:[3,40],queri:[39,43],query_opt:42,quick:[39,43],quickstart:[9,27,39,40,43],rais:14,rand:7,rang:[6,42],rate:[6,43],raw:[6,9,40],rawtransact:[9,40,42],rawtx:[27,40,42],reach:[14,30],realli:0,receiv:[5,6,43],receivepubkei:42,receiverpubkei:42,recommend:3,record:5,reddit:43,redeemscript:42,refer:6,refus:4,regard:6,regtest:6,reindex:7,relai:6,releas:[6,41],reli:3,remov:[6,7],removeoracl:42,removepoolliquid:42,removeprunedfund:42,reorg:6,replac:[6,42],repo:[39,44],report:6,repositori:41,repres:7,reqsig:6,request:[4,5,14,42,43],requir:[4,5,6,8,9,14,43],rescan:[3,42],rescanblockchain:42,reserv:5,resignmasternod:42,resourc:4,restart:6,restor:3,restrict:44,result:[5,6,7],retain:6,retriev:[0,6],reward:[5,6],rewardaddress:42,right:[40,44],root:6,rpc:[6,7,8,27,39,40,41,42,43],rpccach:7,rule:6,run:7,s:[5,6,43],safe:0,same:[6,14,43],satoshi:6,save:3,savemempool:[6,42],scale:6,scan:6,scanobject:[6,42],scantxoutset:[6,42],schnell:43,script:6,scriptaddress:42,scriptpubkei:[6,42],search:[5,9,27],second:[5,6,7],section:[39,41],secur:[0,3],see:[3,6,43],seed:[1,42],seen:[9,27],segwit:6,selb:43,select:[5,6],selectcoin:7,selectionmod:[5,42],sell:44,semant:4,send:[5,8,42],sender:5,sender_address:5,sendmani:42,sendrawtransact:42,sendtoaddress:42,sendtokenstoaddress:[5,42],sendutxosfrom:[5,42],separ:6,sequenc:42,serial:6,server:[4,7],serviceunavail:[4,14],set:[3,5,6,7,14,39],setban:42,setcollateraltoken:42,setdefaultloanschem:42,setgov:[6,42],setgovheight:[6,42],sethdse:[3,42],setlabel:42,setloantoken:42,setnetworkact:42,setoracledata:42,settxfe:42,setup:[9,27],setwalletflag:42,sh:6,shall:44,shareaddress:42,should:[0,3],shown:0,sich:43,sighashtyp:42,sign:42,signal:6,signatur:[6,42],signmessag:42,signmessagewithprivkei:42,signrawtransactionwithkei:42,signrawtransactionwithwallet:42,similar:[4,6],simpl:[9,27,43],simplest:[9,27],sinc:[6,40],singl:[3,5,43],size:6,size_on_disk:6,skip:42,smaller:7,smart:[5,6],so:[3,43,44],softfork:6,softwar:[9,44],sole:3,some:[0,6,7],sometim:6,soon:27,sort:5,specfi:5,special:[6,7],specif:[4,5,6,9,14,27],specifi:[5,6,7,8,9,14,40],speichert:43,spend:[5,6,9],spent:6,spentbi:6,split:42,spring:40,spv:[7,9,40,42],spv_claimhtlc:42,spv_createanchor:42,spv_createanchortempl:42,spv_createhtlc:42,spv_decodehtlcscript:42,spv_dumpprivkei:42,spv_estimateanchorcost:42,spv_getaddresspubkei:42,spv_getalladdress:42,spv_getbal:42,spv_getfeer:42,spv_gethtlcse:42,spv_getnewaddress:42,spv_getpeer:42,spv_getrawtransact:42,spv_gettxconfirm:42,spv_listanchor:42,spv_listanchorauth:42,spv_listanchorreward:42,spv_listanchorrewardconfirm:42,spv_listanchorspend:42,spv_listanchorsunreward:42,spv_listhtlcoutput:42,spv_listreceivedbyaddress:42,spv_listtransact:42,spv_refundhtlc:42,spv_refundhtlcal:42,spv_rescan:42,spv_sendrawtx:42,spv_sendtoaddress:42,spv_syncstatu:42,spv_validateaddress:42,srcaddress1:5,srcaddress2:5,stake:7,stand:43,standard:30,start:[5,6,39,42,43],start_height:42,startbtcheight:42,starttim:6,stat:[6,7,27,40,42],state:[6,7,42,43],statist:[6,7],statu:[6,7,42],step:0,steuern:43,stop:[7,42],stop_height:42,store:[6,43],str:[5,6,7,8,14,30,42],straightforward:43,strength:3,string:[5,6,7,9],strippeds:6,stundensatz:43,subject:[6,44],sublicens:44,submit:5,submitblock:42,submithead:42,subnet:42,subsidi:6,substanti:44,subtractfeefromamount:42,succeed:7,success:6,suggest:[39,43],suitabl:4,sum:[5,6],suppli:5,support:[5,40],sure:[0,3,9,27],swap:[5,7,41,43],swtotal_s:6,swtotal_weight:6,swtx:6,symbol:[5,42],symbol_lookup:[5,42],sync:3,t1:9,t2:9,t:[3,6,39],take:[0,6,9,27,43],takeloan:42,target:6,target_confirm:42,targetratio:42,tax:43,telegram:0,template_request:42,term:[39,44],test:[6,14,40,43],test_connect:14,testen:43,testmempoolaccept:42,testpoolswap:42,text:7,than:[6,7],thank:39,thei:6,them:[0,7,43],therefor:3,thi:[0,2,3,5,6,7,9,14,27,30,39,40,42,44],thing:[9,27],third:5,thorough:6,thread:43,three:[9,27],threshold:6,through:43,thu:[6,7],time:[3,6,7,14,43],timelock:42,timeout:[6,42],timestamp:[6,42],tip:6,to_address:5,to_dusd:5,toaddress:41,token:[5,6,9,27,40,42],tokena:42,tokenamount:42,tokenb:42,tokenfrom:42,tokenid:5,tokensplit:7,tokensymbol:5,tokento:42,tor:7,tort:44,total:[6,7],total_amount:6,total_out:6,total_s:6,total_weight:6,totalfe:6,trade:43,tradeabl:42,transact:[3,5,6,9,27,40,43],transactionid:6,transfer:[5,9],transpar:0,treat:6,tree:6,tri:3,truncat:6,trust:[39,43],tsla:5,ttt:[6,7],turn:0,twitter:[39,43],two:[3,41],tx:6,txcount:6,txhash:42,txid:[6,9,42,43],txindex:6,txn:[5,42],txout:6,txoutproof:42,txrate:6,txtype:[5,42],type:[5,6],typescript:43,typic:5,unabl:4,unauthor:4,unconfirm:6,under:14,understand:43,understood:4,undo:6,unexpect:4,unfortun:0,unharden:6,unit:6,unix:6,unkomplizierter:43,unlimit:5,unloadwallet:42,unlock:42,unprocessableent:4,unspent:6,until:[6,14],unus:7,up:[6,7,39,40],updateloanschem:42,updateloantoken:42,updateoracl:42,updatepoolpair:42,updatetoken:42,updatevault:42,upper:[9,27],uptim:[7,42],uptod:40,url:[14,30],us:[0,1,4,5,6,7,9,14,27,30,39,41,43,44],usabl:14,usag:[6,7],usd:43,usdc:43,user:[9,14,39,41,43,44],util:[3,9,40,42],utxo:[5,6,9],utxo_increas:6,utxo_size_inc:6,utxostoaccount:[5,42],utxoupdatepsbt:42,v0:[6,30],v2:40,valid:[4,6,7],validateaddress:42,valu:[5,6,7,9,42],variabl:6,variou:6,vault:[9,40,42],vaultid:42,verbindung:43,verbos:[5,6,42],veri:[9,27],verif:6,verifi:6,verificationprogress:6,verifychain:[6,42],verifymessag:42,verifytxoutproof:[6,42],version:[6,7,30],versionhex:6,verwendeten:43,via:[14,39,42,43],view:[6,39,41],virtual:6,voll:43,volz:[39,41,43],von:43,vout:[6,9,42],vsize:6,wa:[0,4,6,41],wai:[39,41],wallet:[1,5,9,14,40,42],wallet_nam:[3,14,42],wallet_password:14,wallet_path:14,wallet_timeout:14,walletcreatefundedpsbt:42,walletlock:42,walletpassphras:42,walletpassphrasechang:42,walletprocesspsbt:42,want:[0,9,27,30,39,41,43],warn:6,warranti:[0,3,44],we:[5,6],week:43,weight:6,weightag:42,weiter:43,weitern:43,well:[4,6],welt:43,werden:43,were:[4,6,42],weshalb:43,what:7,when:[0,4,6,7],where:[7,14,30,40],whether:[6,44],which:[0,6,9,14,27,30,42],who:43,whole:5,whom:44,whose:6,wide:43,wiki:2,window:6,window_block_count:6,window_final_block_hash:6,window_final_block_height:6,window_interv:6,window_tx_count:6,wit:6,witch:[14,30,43],with_token:42,withdraw:5,withdrawfromvault:42,withdrawfutureswap:[5,42],without:[0,3,5,7,44],witnessscript:42,won:6,word:5,work:[3,6,43],world:43,would:[0,3],write:[3,39,43],wrongparamet:4,wtxid:6,x:6,xml:7,xprv:6,xpub:6,xx:6,xxx:[6,7],xxxx:6,xxxxx:[6,7],xxxxxx:[6,7],xxxxxxx:7,xxxxxxxx:6,yet:[2,4,6,39,40,43],you:[2,3,6,9,14,27,30,40,41,44],your:[1,5,9,14,27,39,43],yourpassword:14,yourself:3,zero:6,zmq:[7,9,40,42],zu:43,zudem:43,zum:43},titles:["How to get your Light Wallet Private Key","Additional Information","Install Defichain Node","How to use mnemonic seed phrase for your wallet.dat file","Exceptions","Accounts","Blockchain","Control","Generating","Node / RPC","Loan","Masternodes","Mining","Network","Node","Oracles","Poolpair","Rawtransactions","Spv","Tokens","Util","Vault","Wallet","Zmq","Address","Blocks","Fee","Ocean","Loan","Masternodes","Ocean","Oracles","Poolpairs","Prices","RawTx","Rpc","Stats","Tokens","Transactions","DefichainPython","Progress and Updates","Quickstart","Raw Methods Overview","Community","License &amp; Disclaimer"],titleterms:{"0":43,"01":43,"07":43,"1":[0,3,43],"10":0,"11":0,"12":0,"2":[0,3],"2203":43,"3":[0,3,43],"4":[0,3],"5":0,"6":0,"7":0,"8":0,"800":43,"9":0,"\u00fcberblick":43,"default":[9,27],"export":0,"import":[0,3,43],"new":0,A:43,The:43,abov:3,account:5,addit:1,address:[0,9,24],agre:0,all:0,amount:9,announc:43,api:43,ar:[39,43],around:43,ausgegeben:43,bech32:0,beispielaufruf:43,benefit:43,beschreib:43,best:[0,3],big:43,blank:3,block:25,blockchain:6,call:43,cfp:43,click:0,come:43,commun:[39,43],compositswap:43,confirm:0,connect:43,control:7,convert:3,copi:0,corner:0,cost:43,creat:[0,3],da:43,dat:3,defichain:[2,39,41,43],defichainpython:39,den:43,der:43,describ:43,detail:0,develop:43,dfi:43,dies:43,disclaim:[0,3,39,44],displai:0,document:[9,27],doe:43,down:0,enter:0,entwicklungskosten:43,exampl:43,except:4,expert:0,fee:26,file:3,follow:3,format:3,found:0,from:3,fund:43,futur:43,geld:43,gener:[0,3,8],get:0,getblockcount:43,goe:43,ha:43,have:0,here:43,how:[0,3,43],inform:1,input:[9,27],instal:[2,41],introduct:[0,3],jellyfishb:0,kei:0,kommt:43,librari:[39,43],licens:[39,44],light:0,link:43,loan:[10,28],look:39,make:41,marcelkb:43,masternod:[11,29],method:42,mine:12,mnemon:[0,3],mode:0,modul:[9,27],my:0,network:13,newli:3,next:40,node:[2,9,14,40,41],notic:0,ocean:[27,30,41,43],oracl:[15,31],overview:[42,43],packag:[40,41],person:0,phrase:[0,3],pin:0,poolpair:[16,32],practic:[0,3],precondit:43,prepar:0,price:33,privat:0,problem:43,progress:[39,40],project:43,purpos:43,python:[39,41,43],quickstart:41,raw:42,rawtransact:17,rawtx:34,reach:43,recov:3,recoveri:0,releas:43,request:[9,27,41],requir:[0,3],rescanblockchain:3,rest:43,reveal:0,right:0,rpc:[9,35],s:39,saiiv:0,scroll:0,seed:[0,3],select:0,servic:0,set:0,some:43,spent:43,spv:18,start:0,stat:36,step:[3,40],structur:[9,27],term:0,thank:43,thi:43,till:0,toggl:0,token:[19,37],transact:38,type:0,und:43,updat:[39,40],upper:0,us:3,util:20,v1:43,vault:21,verbindungsaufbau:43,version:[40,43],voraussetzung:43,wa:43,wai:0,wait:0,wallet:[0,3,22],welcom:39,what:[39,43],wie:43,wif:3,wird:43,word:3,write:0,you:[0,39,43],your:[0,3],zmq:23,zugut:43,zukunft:43,zweck:43}})