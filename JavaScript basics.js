//Sum of first 10 natural numbers 
let n =10;
let sum=0;
for(let i=0;i<=n;i++)
{
    sum=sum+i;
}
console.log("Total sum : " +sum);

//find max in array without using math library 

let arr=[12,45,7,89,23];
let max=arr[0];
for(let i=0;i<arr.length;i++)
{
    if(arr[i]>max)
    {
        max=arr[i];
    }
}
console.log("Max value in array : " +max);