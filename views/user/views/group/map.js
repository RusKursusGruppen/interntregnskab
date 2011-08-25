function(doc){
    if(doc.type !== "user") return;

    emit([doc.group, doc.username], null);
}
