function insert(item){
	$.ajax({
		type: "POST",
		url: "insert.php",
		data: {name: item}
		alert("Data insert: Success!");
		}
	});
}