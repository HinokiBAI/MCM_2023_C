import * as echarts from 'echarts';

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
  // title: {
  //   text: 'Rainfall vs Evaporation',
  //   subtext: 'Fake Data'
  // },
  // tooltip: {
  //   trigger: 'axis'
  // },
  legend: {
    data: ['Quantity', 'Difficult']
  },
  toolbox: {
    show: true,
    feature: {
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  calculable: true,
  xAxis: [
    {
      type: 'category',
      // prettier-ignore
      data: ['A', 'B1', 'B2', 'C1', 'C2']
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: 'Quantity',
      type: 'bar',
      data: [33, 43, 61, 114, 108],
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    },
    {
      name: 'Difficult',
      type: 'bar',
      data: [0.313 * 210, 0.344 * 210, 0.375 * 210, 0.404 * 210, 98.07],
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    }
  ]
};

option && myChart.setOption(option);
