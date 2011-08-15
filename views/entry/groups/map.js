function(doc) {
    if(doc.type!=="entry") return;
    
    emit([doc.group, doc.date], null);
}
