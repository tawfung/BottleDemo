<h1>LIST OF USERS</h1>
<table>
<tr>
<th>ID</th>
<th>Name</th>
<th>Age</th>
<th>Address</th>
<th>Salary</th>
</tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>