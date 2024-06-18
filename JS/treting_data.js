payload = {
    "documents": [
      {
        "title": "E sign save as template process 2017 1",
        "desc": "",
        "file": {
          "id": "7ohUI8JF1F_2qNARd3jOL0pYjH8hlA",
          "date": "2017-02-21T14:53:46+00:00",
          "processing": null,
          "filename": "e-sign-save-as-template-process-2017-1.pdf",
          "file_size": "1924461",
          "author": {
            "name": "Chris Ward",
            "email": "cw6365@googlemail.com"
          },
          "url": "https://esign-development.s3-eu-west-1.amazonaws.com/uploads/original_file/file/000/052/963/e-sign-save-as-template-process-2017-1.pdf?X-Amz-Expires=600&X-Amz-Date=20170227T174954Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJLGLLV6CP7FXUFRA/20170227/eu-west-1/s3/aws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=274d90e5fef5e495ea89f4ca333a6d3f30ad757d897a1a10713c7dbab53fbdc9",
          "href": "http://esign.dev/api/original_files/7ohUI8JF1F_2qNARd3jOL0pYjH8hlA",
          "thumbnail": "https://esign-development.s3-eu-west-1.amazonaws.com/uploads/document_image/000/707/180/thumb_7ohUI8JF1F_2qNARd3jOL0pYjH8hlA_1.png?X-Amz-Expires=600&X-Amz-Date=20170227T174954Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJLGLLV6CP7FXUFRA/20170227/eu-west-1/s3/aws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=be9bbaf45f32fcacb7328114838a26854f07cab269db8d273643ffe6f5abbdc1"
        },
    "auth_token": "X9bjwyJB7GJPxYnbFGpt"
}
]
}






function deepEqual(object1, object2) {
    const keys1 = Object.keys(object1);
    const keys2 = Object.keys(object2);
  
    //for(const chaves in keys1){  console.log(`keys1.${chaves} = ${keys1[chaves]}`);  }
    if (keys1.length !== keys2.length) {
      return "não tem a mesma quantidade de chaves";
    }
  
    for (const key of keys1) {
      const val1 = object1[key];
      const val2 = object2[key];
      const areObjects = isObject(val1) && isObject(val2);
      if (areObjects && !deepEqual(val1, val2)) {
        return "valores diferente 1";
      }


      if ( !areObjects && val1 !== val2 ) {
        return "valores diferente 2";
      }
    }
  
    return "valores iguais";
  }
  
  function isObject(object) {
    return object != null && typeof object === 'object';
  }


  console.log(deepEqual(payload,payload2));



  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in