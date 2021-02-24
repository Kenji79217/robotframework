let jsonData = JSON.parse(responseBody)
if (jsonData.data) {
    let playRateList = jsonData.data
    
    /*"category": "第四名", "name": "大"*/
    let big = playRateList.find(p => p.code === 's1p3|big')
    if (big) {
        pm.environment.set("NYSC5F-big-playRateId", big.playrateid)
        pm.environment.set("NYSC5F-big-rebate", big.packagemax)
        pm.environment.set("NYSC5F-big-playId", big.playid)
    }
    // /*"category": "第四名", "name": "小"*/
     let small = playRateList.find(p => p.code === 's1p3|small')
     if (small) {
         pm.environment.set("NYSC5F-small-playRateId", small.playrateid)
         pm.environment.set("NYSC5F-small-rebate", small.packagemax)
         pm.environment.set("NYSC5F-small-playId", small.playid)
     }
    // /*"category": "第四名", "name": "单"*/
     let odd = playRateList.find(p => p.code === 's1p3|odd')
     if (odd) {
         pm.environment.set("NYSC5F-odd-playRateId", odd.playrateid)
         pm.environment.set("NYSC5F-odd-rebate", odd.packagemax)
         pm.environment.set("NYSC5F-odd-playId", odd.playid)
     }
    // /*"category": "第四名", "name": "双"*/
     let even = playRateList.find(p => p.code === 's1p3|even')
     if (even) {
         pm.environment.set("NYSC5F-even-playRateId", even.playrateid)
         pm.environment.set("NYSC5F-even-rebate", even.packagemax)
         pm.environment.set("NYSC5F-even-playId", even.playid)
     }
     // /*"category": "第四名", "name": "龍"*/
     let even = playRateList.find(p => p.code === 's1p3|dragon')
     if (even) {
         pm.environment.set("NYSC5F-dragon-playRateId", dragon.playrateid)
         pm.environment.set("NYSC5F-dragon-rebate", dragon.packagemax)
         pm.environment.set("NYSC5F-dragon-playId", dragon.playid)
     }
    // /*"category": "第四名", "name": "虎"*/
     let even = playRateList.find(p => p.code === 's1p3|tiger')
     if (even) {
         pm.environment.set("NYSC5F-tiger-playRateId", tiger.playrateid)
         pm.environment.set("NYSC5F-tiger-rebate", tiger.packagemax)
         pm.environment.set("NYSC5F-tiger-playId", tiger.playid)
     }
    
    // pm.globals.unset("variable_key");
    /*"category": "混合", "name": "大单"*/
    /*let bigodd = playRateList.find(p => p.code === 's1p3|bigodd')
    if (bigodd) {
        pm.environment.set("NYSC5F-bigodd-playRateId", bigodd.playrateid)
        pm.environment.set("NYSC5F-bigodd-rebate", bigodd.packagemax)
        pm.environment.set("NYSC5F-bigodd-playId", bigodd.playid)
    }
    /*"category": "混合", "name": "大双"*/
    /*let bigeven = playRateList.find(p => p.code === 's1p3|bigeven')
    if (bigeven) {
        pm.environment.set("NYSC5F-bigeven-playRateId", bigeven.playrateid)
        pm.environment.set("NYSC5F-bigeven-rebate", bigeven.packagemax)
        pm.environment.set("NYSC5F-bigeven-playId", bigeven.playid)
    }
    /*"category": "混合", "name": "小单"*/
    /*let smallodd = playRateList.find(p => p.code === 's1p3|smallodd')
    if (smallodd) {
        pm.environment.set("NYSC5F-smallodd-playRateId", smallodd.playrateid)
        pm.environment.set("NYSC5F-smallodd-rebate", smallodd.packagemax)
        pm.environment.set("NYSC5F-smallodd-playId", smallodd.playid)
    }
    /*"category": "混合", "name": "小双"*/
    /*let smalleven = playRateList.find(p => p.code === 's1p3|smalleven')
    if (smalleven) {
        pm.environment.set("NYSC5F-smalleven-playRateId", smalleven.playrateid)
        pm.environment.set("NYSC5F-smalleven-rebate", smalleven.packagemax)
        pm.environment.set("NYSC5F-smalleven-playId", smalleven.playid)
    }
     /*"category": "混合", "name": "极大"*/
    /*let max = playRateList.find(p => p.code === 's1p3|max')
    if (max) {
        pm.environment.set("NYSC5F-max-playRateId", max.playrateid)
        pm.environment.set("NYSC5F-max-rebate", max.packagemax)
        pm.environment.set("NYSC5F-max-playId", max.playid)
    }
     /*"category": "混合", "name": "极小"*/
    /*let min = playRateList.find(p => p.code === 's1p3|min')
    if (min) {
        pm.environment.set("NYSC5F-min-playRateId", min.playrateid)
        pm.environment.set("NYSC5F-min-rebate", min.packagemax)
        pm.environment.set("NYSC5F-min-playId", min.playid)
    }
     /*"category": "混合", "name": "豹子"*/
    /*let triples = playRateList.find(p => p.code === 'tmb3|triples')
    if (triples) {
        pm.environment.set("NYSC5F-triples-playRateId", triples.playrateid)
        pm.environment.set("NYSC5F-triples-rebate", triples.packagemax)
        pm.environment.set("NYSC5F-triples-playId", triples.playid)
    }
    /*"category": "混合", "name": "蓝波"*/
    /*let blue = playRateList.find(p => p.code === 'tmcolor|blue')
    if (blue) {
        pm.environment.set("NYSC5F-blue-playRateId", blue.playrateid)
        pm.environment.set("NYSC5F-blue-rebate", blue.packagemax)
        pm.environment.set("NYSC5F-blue-playId", blue.playid)
    }
    /*"category": "混合", "name": "红波"*/
    /*let red = playRateList.find(p => p.code === 'tmcolor|red')
    if (red) {
        pm.environment.set("NYSC5F-red-playRateId", red.playrateid)
        pm.environment.set("NYSC5F-red-rebate", red.packagemax)
        pm.environment.set("NYSC5F-red-playId", red.playid)
    }
     /*"category": "混合", "name": "綠波"*/
    /*let green = playRateList.find(p => p.code === 'tmcolor|green')
    if (green) {
        pm.environment.set("NYSC5F-green-playRateId", green.playrateid)
        pm.environment.set("NYSC5F-green-rebate", green.packagemax)
        pm.environment.set("NYSC5F-green-playId", green.playid)
    }
    /*"category": "混合", "name": "０"*/
    /*let tm0 = playRateList.find(p => p.code === 's1p3|0')
    if (tm0) {
        pm.environment.set("NYSC5F-tm0-playRateId", tm0.playrateid)
        pm.environment.set("NYSC5F-tm0-rebate", tm0.packagemax)
        pm.environment.set("NYSC5F-tm0-playId", tm0.playid)
    }
     /*"category": "混合", "name": "1"*/
    /*let tm1 = playRateList.find(p => p.code === 's1p3|1')
    if (tm1) {
        pm.environment.set("NYSC5F-tm1-playRateId", tm1.playrateid)
        pm.environment.set("NYSC5F-tm1-rebate", tm1.packagemax)
        pm.environment.set("NYSC5F-tm1-playId", tm1.playid)
    }
     /*"category": "混合", "name": "2"*/
    /*let tm2 = playRateList.find(p => p.code === 's1p3|2')
    if (tm2) {
        pm.environment.set("NYSC5F-tm2-playRateId", tm2.playrateid)
        pm.environment.set("NYSC5F-tm2-rebate", tm2.packagemax)
        pm.environment.set("NYSC5F-tm2-playId", tm2.playid)
    }*/
	

	
}


