function chart_8(score_list){

    var myChart8 = echarts.init(document.getElementById('test8'));
    option = {
        backgroundColor: 'rgba(0,0,0,0)',
        legend: {
            top: 10,
            textStyle: {
                color: '#fff',
            },
            data: ['previous score', 'current score']
        },
        grid: {
            left: '3%',
            right: '3%',
            bottom: '3%',
            containLabel: true
        },

        tooltip: {
            show: "true",
            trigger: 'item',
            backgroundColor: 'rgba(0,0,0,0.7)', // 背景
            padding: [8, 10], //内边距
            extraCssText: 'box-shadow: 0 0 3px rgba(255, 255, 255, 0.4);', //添加阴影
            formatter: function(params) {
                if (params.seriesIndex == "3" || params.seriesIndex == "4" || params.seriesIndex == "5") {
                    return params.name + '<br>' + params.seriesName + ' ： 第 ' + params.value + ' 名';
                }
            }
        },
        yAxis: {
            type: 'value',
            axisTick: {
                show: false
            },
            axisLine: {
                show: true,
                lineStyle: {
                    color: '#363e83',
                }
            },
            splitLine: {
                show: true,
                lineStyle: {
                    color: '#363e83 ',
                    type: 'dotted'
                }
            },
            axisLabel: {
                textStyle: {
                    color: '#fff',
                    fontWeight: 'normal',
                    fontSize: '12',
                },
            },
        },
        xAxis: [{
                type: 'category',
                axisTick: {
                    show: false
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#363e83',
                    }
                },
                axisLabel: {
                    inside: false,
                    textStyle: {
                        color: '#fff',
                        fontWeight: 'normal',
                        fontSize: '12',
                    },
                },
                data: ['Clothing', 'Jewelry', 'Shoes', 'Watches']
            }, {
                type: 'category',
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    show: false
                },
                splitArea: {
                    show: false
                },
                splitLine: {
                    show: false
                },
                data: ['Clothing', 'Jewelry', 'Shoes', 'Watches']
            },

        ],
        series: [{
                name: 'previous score',
                type: 'bar',
                itemStyle: {
                    normal: {
                        show: true,
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: '#f7734e'
                        }, {
                            offset: 1,
                            color: '#e12945'
                        }]),
                        barBorderRadius: 20,
                        borderWidth: 0,
                    }
                },
                zlevel: 2,
                barWidth: '7%',
                data: score_list[0]
            }, {
                name: 'current score',
                type: 'bar',
                barWidth: '7%',
                itemStyle: {
                    normal: {
                        show: true,
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: '#96d668'
                        }, {
                            offset: 1,
                            color: '#01babc'
                        }]),
                        barBorderRadius: 20,
                        borderWidth: 0,
                    }
                },
                zlevel: 2,
                barGap: '100%',
                data: score_list[1]
            }

        ]
    };
    myChart8.setOption(option);
}

// ------------
function chart_2(cl_sale,je_sale,sh_sale,wa_sale){

    var myChart2 = echarts.init(document.getElementById('test2'));
    var giftImageUrl = 'data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDIxLjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IuWbvuWxgl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgMjAyLjcgMjAyLjUiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDIwMi43IDIwMi41OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGw6I0ZGRkZGRjt9Cjwvc3R5bGU+CjxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0xMjMuMyw1OS41YzAtMS44LTEuNS0zLjItMy40LTMuMkgxNy40Yy0xLjksMC0zLjQsMS40LTMuNCwzLjJ2NTVoMTA5LjNWNTkuNUwxMjMuMyw1OS41eiBNMTQ4LjQsMTIyLjMKCWMtNywwLTEyLjYsNS40LTEyLjYsMTJjMCw2LjYsNS42LDEyLDEyLjYsMTJzMTIuNi01LjQsMTIuNi0xMkMxNjEsMTI3LjYsMTU1LjQsMTIyLjMsMTQ4LjQsMTIyLjN6IE00Ny44LDEyMi4zCgljLTcsMC0xMi42LDUuNC0xMi42LDEyYzAsNi42LDUuNiwxMiwxMi42LDEyczEyLjYtNS40LDEyLjYtMTJDNjAuNCwxMjcuNiw1NC44LDEyMi4zLDQ3LjgsMTIyLjN6IE0zOS45LDExOS4ySDE0VjEzMQoJYzAsMS44LDEuNSwzLjIsMy40LDMuMmgxMi44QzMwLjIsMTI3LjcsMzQuMiwxMjIsMzkuOSwxMTkuMnogTTE4MC4zLDExMS4xbC0yMC45LTMyLjljLTEtMS41LTMuMi0yLjctNS4xLTIuN2gtMjIuNQoJYy0xLjksMC0zLjQsMS40LTMuNCwzLjJ2NDAuNkg1NS44YzUuNywyLjgsOS43LDguNSw5LjcsMTVoNjUuM2MwLTkuMyw3LjktMTYuOCwxNy42LTE2LjhTMTY2LDEyNSwxNjYsMTM0LjNoMTIuNgoJYzEuOSwwLDMuNC0xLjQsMy40LTMuMlYxMTdDMTgyLjEsMTE1LjMsMTgxLjMsMTEyLjYsMTgwLjMsMTExLjF6IE0xNjUuOSwxMDMuM2wtMjkuMi0zLjJjLTAuOS0wLjEtMS43LTAuOS0xLjctMS44VjgzLjQKCWMwLTAuOSwwLjgtMS42LDEuNy0xLjZoMTUuNGMxLDAsMi4xLDAuNiwyLjYsMS40bDEyLDE4LjhDMTY3LjIsMTAyLjgsMTY2LjgsMTAzLjMsMTY1LjksMTAzLjN6Ii8+Cjwvc3ZnPgo=';
    option = {
        backgroundColor: 'rgba(0,0,0,0)',
        tooltip: {
            trigger: 'item',
            formatter: "{b} : {d}% / {c}"
        },
        graphic: {
            elements: [{
                type: 'image',
                style: {
                    image: giftImageUrl,
                    width: 50,
                    height: 50
                },
                left: 'center',
                top: 'center'
            }]
        },
        legend: {
            orient: 'horizontal',
            icon: 'circle',
            bottom: 5,
            x: 'center',
            textStyle: {
                color: '#fff'
            },
            data: ['Clothing', 'Jewelry', 'Shoes', 'Watches']
        },
        series: [{
            type: 'pie',
            radius: ['38%', '48%'],
            center: ['50%', '50%'],
            color: ['#0E7CE2', '#FF8352', '#E271DE', '#F8456B', '#00FFFF', '#4AEAB0'],
            data: [{
                    value: cl_sale,
                    name: 'Clothing'
                },
                {
                    value: je_sale,
                    name: 'Jewelry'
                },
                {
                    value: sh_sale,
                    name: 'Shoes'
                },
                {
                    value: wa_sale,
                    name: 'Watches'
                }
            ],
            labelLine: {
                normal: {
                    show: true,
                    length: 20,
                    length2: 20,
                    lineStyle: {
                        color: '#363c88',
                        width: 1
                    }
                }
            },
            label: {
                normal: {
                    formatter: '{c|{c}units}\n{hr|}\n{d|{d}%}',
                    rich: {
                        b: {
                            fontSize: 12,
                            color: '#12EABE',
                            align: 'left',
                            padding: 4
                        },
                        hr: {
                            borderColor: '#363c88',
                            width: '100%',
                            borderWidth: 1,
                            height: 0
                        },
                        d: {
                            fontSize: 12,
                            color: '#fff',
                            align: 'left',
                            padding: 4
                        },
                        c: {
                            fontSize: 12,
                            color: 'rgba(255,255,2555,.7)',
                            align: 'center',
                            padding: 4
                        }
                    }
                }
            }
        }]
    };
    myChart2.setOption(option);
}
// ------------ chart_3
function chart_3(data_percent){
    var myChart3 = echarts.init(document.getElementById('test3'));
    option = {
        series: [{
                name: ' clothing',
                type: 'pie',
                radius: ['52%', '66%'],
                center: ['50%', '44%'],
                startAngle: 225,
                color: [new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#FEB692'
                }, {
                    offset: 1,
                    color: '#EA5455'
                }]), "transparent"],
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: data_percent,
                    name: 'clothing',
                    label: {
                        normal: {
                            formatter: 'percentage',
                            textStyle: {
                                color: '#fff',
                                fontSize: 11

                            }
                        }
                    }
                }, {
                    value: 100-data_percent,
                    name: '%',
                    label: {
                        normal: {
                            formatter: '\n'+data_percent+'%',
                            textStyle: {
                                color: '#0ec4d0',
                                fontSize: 14

                            }
                        }
                    }
                }]
            },

        ]
    };
    myChart3.setOption(option);
}
// ---------------
function chart_4(data_percent){

    var myChart4 = echarts.init(document.getElementById('test4'));
    option = {
        series: [{
                name: ' 报警车辆占比',
                type: 'pie',
                radius: ['52%', '66%'],
                center: ['50%', '44%'],
                startAngle: 225,
                color: [new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#CE9FFC'
                }, {
                    offset: 1,
                    color: '#7367F0'
                }]), "transparent"],
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: data_percent,
                    name: '占比',
                    label: {
                        normal: {
                            formatter: 'percentage',
                            textStyle: {
                                color: '#fff',
                                fontSize: 11

                            }
                        }
                    }
                }, {
                    value: 100-data_percent,
                    name: '%',
                    label: {
                        normal: {
                            formatter: '\n'+data_percent+'%',
                            textStyle: {
                                color: '#0ec4d0',
                                fontSize: 14

                            }
                        }
                    }
                }]
            },

        ]
    };
    myChart4.setOption(option);
}
//----------------
function chart_5(data_percent){

    var myChart5 = echarts.init(document.getElementById('test5'));
    option = {
        series: [{
                name: ' 上线车辆占比',
                type: 'pie',
                radius: ['52%', '66%'],
                center: ['50%', '44%'],
                startAngle: 225,
                color: [new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#5EFCE8'
                }, {
                    offset: 1,
                    color: '#736EFE'
                }]), "transparent"],
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: data_percent,
                    name: '上线车辆占比',
                    label: {
                        normal: {
                            formatter: 'percentage',
                            textStyle: {
                                color: '#fff',
                                fontSize: 11

                            }
                        }
                    }
                }, {
                    value: 100-data_percent,
                    name: '%',
                    label: {
                        normal: {
                            formatter: '\n'+data_percent+'%',
                            textStyle: {
                                color: '#0ec4d0',
                                fontSize: 14

                            }
                        }
                    }
                }]
            },

        ]
    };
    myChart5.setOption(option);
}
//----------------
function chart_6(data_percent){

    var myChart6 = echarts.init(document.getElementById('test6'));
    option = {
        series: [{
                name: ' 在线车辆占比',
                type: 'pie',
                radius: ['52%', '66%'],
                center: ['50%', '44%'],
                startAngle: 225,
                color: [new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#43CBFF'
                }, {
                    offset: 1,
                    color: '#9708CC'
                }]), "transparent"],
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: data_percent,
                    name: '在线车辆占比',
                    label: {
                        normal: {
                            formatter: 'percentage',
                            textStyle: {
                                color: '#fff',
                                fontSize: 11

                            }
                        }
                    }
                }, {
                    value: 100 - data_percent,
                    name: '%',
                    label: {
                        normal: {
                            formatter: '\n'+data_percent+'%',
                            textStyle: {
                                color: '#0ec4d0',
                                fontSize: 14

                            }
                        }
                    }
                }]
            },

        ]
    };
    myChart6.setOption(option);
}
//------------------
function chart_1(dic_pred_time_js,dic_pred_pre_js,dic_pred_cur_js){

    // dic_pred_time_js
    var obj_dic_pred_time_js = eval("(" + dic_pred_time_js + ")");
    var arr_dic_pred_time_js = []
    for (var key in obj_dic_pred_time_js) {
        var item = obj_dic_pred_time_js[key];
        arr_dic_pred_time_js.push(item)
        }

    // dic_pred_pre_js
    var obj_dic_pred_pre_js = eval("(" + dic_pred_pre_js + ")");
    var arr_dic_pred_pre_js = []
    for (var key in obj_dic_pred_pre_js) {
        var item = obj_dic_pred_pre_js[key];
        arr_dic_pred_pre_js.push(item)
        }

    // dic_pred_cur_js
    var obj_dic_pred_cur_js = eval("(" + dic_pred_cur_js + ")");
    var arr_dic_pred_cur_js = []
    for (var key in obj_dic_pred_cur_js) {
        var item = obj_dic_pred_cur_js[key];
        arr_dic_pred_cur_js.push(item)
        }
    
    var myChart1 = echarts.init(document.getElementById('test1'));
    var charts = {
        unit: 'Kbps',
        names: ['sale_prediction', 'sale_actual'],
        lineX: arr_dic_pred_time_js,
        value: [
            arr_dic_pred_pre_js,
            arr_dic_pred_cur_js
        ]

    }
    var color = ['rgba(255,100,97', 'rgba(23, 255, 243']
    var lineY = []

    for (var i = 0; i < charts.names.length; i++) {
        var x = i
        if (x > color.length - 1) {
            x = color.length - 1
        }
        var data = {
            name: charts.names[i],
            type: 'line',
            color: color[x] + ')',
            smooth: true,
            areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: color[x] + ', 0.3)'
                    }, {
                        offset: 0.8,
                        color: color[x] + ', 0)'
                    }], false),
                    shadowColor: 'rgba(0, 0, 0, 0.1)',
                    shadowBlur: 10
                }
            },
            symbol: 'circle',
            symbolSize: 5,
            data: charts.value[i]
        }
        lineY.push(data)
    }

    var option = {
            backgroundColor: 'rgba(255,255,255,0)',
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: charts.names,
                textStyle: {
                    fontSize: 12,
                    color: 'rgb(0,253,255,0.6)'
                },
                top: 20,
                right: 50
            },
            grid: {
                left: 24,
                right: 54,
                bottom: 20,
                top: 60,
                containLabel: true
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: charts.lineX,
                axisLine: {
                    lineStyle: {
                        color: '#363e83 ',
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: '#fff'
                    },
                }
            },
            yAxis: {
                name: charts.unit,
                type: 'value',
                min: function(value) {
                    return value.min - 100;
                },
                axisLabel: {
                    formatter: '{value}',
                    textStyle: {
                        color: '#fff'
                    }
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#363e83 ',
                        type: 'dotted'
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#363e83 ',
                    }
                }
            },
            series: lineY
        }

    setInterval(function() {
        myChart1.setOption({
            legend: {
                selected: {
                    'sale_prediction': false,
                    'sale_actual': false
                }
            }
        })
        myChart1.setOption({
            legend: {
                selected: {
                    'sale_prediction': true,
                    'sale_actual': true
                }
            }
        })
    }, 10000)
    myChart1.setOption(option);
}

//------------------
function chart_7(word_list_js){
    var chart = echarts.init(document.getElementById('test7'));
    var obj_1 = eval("(" + word_list_js + ")");
    var arr1 = []
    for (var key in obj_1) {
        var item = obj_1[key];
        arr1.push(item)
        }
    

    var option = {
        tooltip: {},
        series: [ {
            type: 'wordCloud',
            gridSize: 2,
            sizeRange: [10, 100],
            rotationRange: [-90, 90],
            shape: 'pentagon',
            width: 600,
            height: 200,
            drawOutOfBound: true,
            textStyle: {
                color: function () {
                    return 'rgb(' + [
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160)
                    ].join(',') + ')';
                }
            },
            emphasis: {
                textStyle: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: arr1
        } ]
    };

    chart.setOption(option);

    window.onresize = chart.resize;

}   

// 自适应
// window.addEventListener("resize", function() {
//     myChart1.resize();
//     myChart2.resize();
//     myChart3.resize();
//     myChart4.resize();
//     myChart5.resize();
//     myChart6.resize();
//     myChart7.resize();
//     myChart8.resize();
// });