function pal(str){

    let count = {}

    str.split("").forEach(el => {
      if(count[el] == undefined || count[el] == 0){
        count[el] = 1;
      } else {
        count[el] = 0;
      }
    });

    let sum  = 0;
    console.log(count);
    for (let o in count) {
      sum += count[o];
    }

    console.log(sum);
    if(str.length % 2 === 0 && sum === 0){
      return true;
    }
    if(str.length % 2 ===  1 && sum === 1){
      return true;
    }
  return false;


}
