// Code goes here
angular.module("app", ["chart.js"]).controller("BarCtrl", function ($scope, $http) {

  $scope.labelsProduct = ['ProductA', 'ProductB', 'ProductA1', 'ProductB1'];
  $scope.labelsProductOne = ['ProductA'];
  $scope.labelsProductTwo = ['ProductB'];
  $scope.labelsProductThree = ['ProductA1'];
  $scope.labelsProductFour = ['ProductB1'];
  $scope.labelsCompany = ['CompanyX', 'CompanyY'];
  $scope.labelsCompanyOne = ['CompanyX'];
  $scope.labelsCompanyTwo = ['CompanyY'];
  $scope.series = ['Postive', 'Negative'];
  $scope.options = {
    legend: {
      display: true,
      position: 'bottom'
    },
    cutoutPercentage: 60,
    tooltipEvents: [],
    tooltipCaretSize: 0,
    showTooltips: true,
    onAnimationComplete: function() {
      self.showTooltip(self.segments, true);
    }
  }
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];
  $scope.optionsOne = {
    scales: {
      yAxes: [
        {
          id: 'y-axis-1',
          type: 'linear',
          display: true,
          position: 'left'
        },
        {
          id: 'y-axis-2',
          type: 'linear',
          display: true,
          position: 'right'
        }
      ]
    }
  };
  $scope.chartOptions = {
    legend: {
      display: true
    },
    scales: {
      yAxes: [{ id: 'y-axis-1', type: 'linear', position: 'left', ticks: { min: 0, max: 100 } }]
    }
  };
  
   $scope.chartOptionsLine = {
    legend: {
      display: true
    },
    scales: {
      xAxes: [{ id: 'x-axis-1', type: 'linear', position: 'bottom', ticks: { min: 0, max: 100 } }]
    }
  };
  
  
  
  
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };

  $http.get('http://localhost:5004/').then(function (response) {
    console.log("inside rest call")
    ds = response.data;
    angular.forEach(ds, function (value, key) {
      if (value.company == 'CompanyX' && value.product == '') {
        $scope.companyXP = value.positive;
        $scope.companyXN = value.negative;
      }
      if (value.company == 'CompanyY' && value.product == '') {
        $scope.companyYP = value.positive;
        $scope.companyYN = value.negative;
      }
      if (value.company == 'CompanyX' && value.product == 'ProductA') {
        $scope.companyXProdAP = value.positive;
        $scope.companyXProdAN = value.negative;
      }
      if (value.company == 'CompanyX' && value.product == 'ProductB') {
        $scope.companyXProdBP = value.positive;
        $scope.companyXProdBN = value.negative;
      }
      if (value.company == 'CompanyY' && value.product == 'A1') {
        $scope.companyYProdA1P = value.positive;
        $scope.companyYProdA1N = value.negative;
      }
      if (value.company == 'CompanyY' && value.product == 'B1') {
        $scope.companyYProdB1P = value.positive;
        $scope.companyYProdB1N = value.negative;
      }
    });

    $scope.dataProduct = [
      [$scope.companyXProdAP, $scope.companyXProdBP, $scope.companyYProdA1P, $scope.companyYProdB1P],
      [$scope.companyXProdAN, $scope.companyXProdBN, $scope.companyYProdA1N, $scope.companyYProdB1N]
    ];
	$scope.dataCompany = [
      [$scope.companyXP, $scope.companyYP],
      [$scope.companyXN, $scope.companyYN]
    ];
	$scope.dataCompanyOne = [
      [$scope.companyXP],
      [$scope.companyXN]
    ];
	$scope.dataCompanyTwo = [
      [$scope.companyYP],
      [$scope.companyYN]
    ];
	 $scope.dataProductOne = [
      [$scope.companyXProdAP],
      [$scope.companyXProdAN]
    ];
	 $scope.dataProductTwo = [
      [$scope.companyXProdBP],
      [$scope.companyXProdBN]
    ];
	 $scope.dataProductThree = [
      [$scope.companyYProdA1P],
      [$scope.companyYProdA1N]
    ];
	 $scope.dataProductFour = [
      [$scope.companyYProdB1P],
      [$scope.companyYProdB1N]
    ];
  });

});