<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.3.15/angular.min.js"></script>
<script src="static/angular-datatables.min.js"></script>
<script src="static/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
<link rel="stylesheet" href="static/datatables.bootstrap.css">
</head>
<body ng-app="TestApp" ng-controller="testController">

<div class="container">
<h1>Demo : Simple Demo of datatable with angular Application</h1>
  <table class="table table-striped table-bordered" datatable="ng" dt-options="vm.dtOptions">
    <thead>
      <tr><th>Sr</th><th>Name</th><th>Age</th><th>Action</th></tr>
    </thead>
    <tbody>
      <tr ng-repeat="user in userList">
        <td>{{$index + 1}}</td>
        <td>{{user.Name}}</td>
        <td>{{user.Age}}</td>
		<td><div class="btn-group">
                <button type="button" class="btn btn-default btn" ng-click="edit($index);"><i class="glyphicon glyphicon-pencil"></i></button>
                <button type="button" class="btn btn-default btn" ng-click="delete();"><i class="glyphicon glyphicon-trash"></i></button>
                </div></td>
      </tr>
    </tbody>
  </table>
  </div>
</body>
</html>
<script>
angular.module('TestApp', ['TestApp.controllers','datatables']);

	angular.module('TestApp.controllers', []).controller('testController', function($scope,DTOptionsBuilder, DTColumnBuilder) {
		$scope.userList = [
			  {

				  Name: 'Parvez Alam',
				  Age: '28'
			  },

			 {
				Name: 'Sameer',
				Age: '13'
			  },
			  {
				Name: 'Rakesh',
				Age: '55'
			  },
			  {
				Name: 'Ramesh',
				Age: '44'
			  },
			  {
				Name: 'Aman',
				Age: '34'
			  },
			  {
				Name: 'John',
				Age: '23'
			  },
			  {

				  Name: 'Parvez Alam',
				  Age: '28'
			  },

			 {
				Name: 'Rajesh',
				Age: '13'
			  },
			  {
				Name: 'Mohit',
				Age: '12'
			  },
			  {
				Name: 'Riyaj',
				Age: '44'
			  },
			  {
				Name: 'Nisha',
				Age: '34'
			  },
			  {
				Name: 'Neha',
				Age: '23'
			  }
		  ];

		$scope.vm = {};

		$scope.vm.dtOptions = DTOptionsBuilder.newOptions()
		  .withOption('order', [0, 'asc']);
		 });

</script>
