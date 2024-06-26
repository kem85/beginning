let job="Manager";
let salary = 0;
switch(job)
{
    case "Manager":
        salary = 8000;
        break;
    case "IT"||"Support":
        salary = 6000;
        break;
    case "Developer" || "Designer":
        salary = 7000;
        break;
    default:
        salary=4000;
}
console.log(salary);