int question()
{
    timer();
     while(true)
    {
    sdsd:
    g=rando(1,3);
    if(g==repeat){goto sdsd;}
    else{
    s=(g==1) ? "A" : (g==2) ? "B":"C";
    cout<<rando(1,255)<<"."<<rando(30,155)<<"."<<rando(20,90)<<"."<<rando(1,255)<<endl;
     cout<<"Class: "<<s<<endl;
        cin>>x;
    }
    repeat=g;
    cout<<"You finished in: "<<minutes<<" minutes "<<seconds<<" seconds"<<endl;
    minutes=0;seconds=0;
    }
}