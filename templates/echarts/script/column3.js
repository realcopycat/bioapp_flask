/** pear-admin-v3.10.0 MIT License By http://www.pearadmin.com/ */
 ;"use strict";layui.use(["echarts"],(function(){var t=layui.echarts.init(document.getElementById("column3"),null,{width:600,height:400});option={backgroundColor:"#fff",tooltip:{trigger:"axis",padding:[8,10],backgroundColor:"rgba(255,255,255,0.5)",axisPointer:{type:"shadow",color:"#fff"}},legend:{data:["新开会员","激活会员","关闭会员"],align:"left",right:0,color:"#333",fontSize:14,fontWeight:200,itemWidth:14,itemHeight:14,itemGap:35},grid:{left:"0",right:"0",bottom:"8%",top:"15%",containLabel:!0},label:{show:!0,position:"top",color:"#333",fontSize:14,fontWeight:700},xAxis:[{type:"category",offset:10,data:["团队1","团队2","团队3","团队4"],axisLine:{show:!1},axisTick:{show:!1},axisLabel:{show:!0,color:"#333",fontSize:16,fontWeight:200}}],yAxis:[{type:"value",axisLabel:{show:!1},axisTick:{show:!1},axisLine:{show:!1},splitLine:{show:!1}}],series:[{name:"新开会员",type:"bar",data:[20,34,18,14,16],barWidth:22,barGap:1,itemStyle:{color:"#0071c8",opacity:1}},{name:"激活会员",type:"bar",data:[10,24,5,24,16],barWidth:22,barGap:1,itemStyle:{color:"#fdc508",opacity:1}},{name:"关闭会员",type:"bar",data:[7,24,18,20,6],barWidth:22,barGap:1,itemStyle:{color:"#dfeafc",opacity:1}}]},t.setOption(option),window.onresize=function(){t.resize()}}));