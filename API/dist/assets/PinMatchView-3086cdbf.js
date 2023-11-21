import{r as u,b as o,e as r,f as e,j as n,q as v,F as g,x as y,v as d,m as p,n as C,l as c,p as w}from"./index-d8ac051c.js";import{a as k}from"./axios-47b9d439.js";const S=e("h2",{class:"p-2 text-2xl font-bold text-center"},"PL Pin Match ",-1),V=["onSubmit"],E={class:"w-full m-2 border border-gray-200 rounded-lg bg-gray-50"},U={class:"p-3 grid gap-4 md:grid-cols-2"},B=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"App year ",-1),A=["value"],M=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"App month ",-1),L=["value"],q=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"Staging Database ",-1),P=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"Staging Schema",-1),R=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"Staging S3 Bucket",-1),D=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"Staging S3 Prefix",-1),N=e("label",{class:"block mb-2 text-sm font-medium text-rose-600"},"Username",-1),T={class:"flex items-center justify-between px-3 py-2"},H=["disabled"],Z={key:0,"aria-hidden":"true",role:"status",class:"inline w-4 h-4 me-3 text-white animate-spin",viewBox:"0 0 100 101",fill:"none",xmlns:"http://www.w3.org/2000/svg"},j=e("path",{d:"M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z",fill:"#E5E7EB"},null,-1),F=e("path",{d:"M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z",fill:"currentColor"},null,-1),I=[j,F],K={key:0,class:"text-red-600"},J=["src"],Q={__name:"PinMatchView",setup(O){const s=u({USER:"Elly",year:"",month:"",db:"BE_SCRATCH",schm:"EARABMAKKI",s3:"mf-datascience",prefix:"ascend_pin_matching/transfer_data/new"}),a=u({label:"Start Process",isLoading:!1}),f=u(""),_=async()=>{const x="/proxy/8000/pinmatch";a.value.isLoading=!0,a.value.label="Loading...";try{const l=await k.post(x,s.value);i.value=l.data.message,f.value=l.data.flow_status_link}catch(l){i.value=l,console.error(l)}finally{a.value.isLoading=!1,a.value.label="Start Process"}},b=u(!1),h=()=>b.value=!b.value,i=u("");return(x,l)=>(o(),r(g,null,[S,e("form",{onSubmit:w(_,["prevent"])},[e("div",E,[e("div",U,[e("div",null,[B,n(e("select",{id:"countries","onUpdate:modelValue":l[0]||(l[0]=t=>s.value.year=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 hover:cursor-pointer"},[(o(!0),r(g,null,y(Array.from({length:11},(t,m)=>2023-m),t=>(o(),r("option",{value:t},c(t),9,A))),256))],512),[[v,s.value.year]])]),e("div",null,[M,n(e("select",{id:"countries","onUpdate:modelValue":l[1]||(l[1]=t=>s.value.month=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 hover:cursor-pointer"},[(o(!0),r(g,null,y(Array.from({length:11},(t,m)=>11-m),t=>(o(),r("option",{value:t},c(t),9,L))),256))],512),[[v,s.value.month]])]),e("div",null,[q,n(e("input",{type:"text","onUpdate:modelValue":l[2]||(l[2]=t=>s.value.db=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",placeholder:"BE_SCRATCH",required:""},null,512),[[d,s.value.db]])]),e("div",null,[P,n(e("input",{type:"text","onUpdate:modelValue":l[3]||(l[3]=t=>s.value.schm=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",placeholder:"DJOHN",required:""},null,512),[[d,s.value.schm]])]),e("div",null,[R,n(e("input",{type:"text","onUpdate:modelValue":l[4]||(l[4]=t=>s.value.s3=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",required:""},null,512),[[d,s.value.s3]])]),e("div",null,[D,n(e("input",{type:"text","onUpdate:modelValue":l[5]||(l[5]=t=>s.value.prefix=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",required:""},null,512),[[d,s.value.prefix]])]),e("div",null,[N,n(e("input",{type:"text","onUpdate:modelValue":l[6]||(l[6]=t=>s.value.USER=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",required:""},null,512),[[d,s.value.USER]])])]),e("div",T,[e("button",{disabled:a.value.isLoading,type:"submit",class:"m-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 inline-flex items-center"},[a.value.isLoading?(o(),r("svg",Z,I)):p("",!0),C(),e("span",null,c(a.value.label),1)],8,H),i.value?(o(),r("div",K,[e("span",null,c(i.value),1),e("button",{type:"button",class:"m-1 px-1 rounded-md text-blue-700",onClick:h}," show status")])):p("",!0)])])],40,V),e("div",null,[b.value?(o(),r("iframe",{key:0,src:f.value,class:"w-full min-h-screen",frameborder:"1"},null,8,J)):p("",!0)])],64))}};export{Q as default};