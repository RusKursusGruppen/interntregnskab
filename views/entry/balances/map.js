function(doc) {
    if(doc.type!=="entry") return;
    if(doc.deletedby!==undefined && doc.deletedby!==null) return;
    
    var weight_total = 0;

    doc.debtors.forEach(function(x){
        weight = x[1];
        weight_total += x[1];
    });

    if(weight_total == 0) return;
    
    var remaining_amount = doc.amount;

    emit([doc.group, doc.creditor, doc.date], doc.amount);
    doc.debtors.forEach(function(x){
        name = x[0];
        weight = x[1];
        
        var amount = Math.floor((remaining_amount * weight) / weight_total);

        remaining_amount -= amount;
        weight_total -= weight;

        emit([doc.group, name, doc.date], -amount);
    });
}
