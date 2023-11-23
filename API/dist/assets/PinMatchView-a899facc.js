import{r as d,o as w,w as C,b as o,e as s,f as e,j as u,q as h,F as x,x as y,v as b,m,n as k,l as f,k as S,p as V}from"./index-082e2622.js";import{a as M}from"./axios-47b9d439.js";const B=e("h2",{class:"p-2 text-2xl font-bold text-center"},"PL Pin Match ",-1),U=["onSubmit"],A={class:"w-full m-2 border border-gray-200 rounded-lg bg-gray-50"},L={class:"p-3 grid gap-4 md:grid-cols-2"},P=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"App year ",-1),E=["value"],q=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"App month ",-1),D=["value"],N=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"Database ",-1),T=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"Schema",-1),H=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"S3 Bucket",-1),I=e("label",{class:"block mb-2 text-sm font-medium text-gray-600"},"S3 Prefix",-1),R={class:"flex items-center justify-between px-3 py-2"},Z=["disabled"],j={key:0,"aria-hidden":"true",role:"status",class:"inline w-4 h-4 me-3 text-white animate-spin",viewBox:"0 0 100 101",fill:"none",xmlns:"http://www.w3.org/2000/svg"},F=e("path",{d:"M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z",fill:"#E5E7EB"},null,-1),J=e("path",{d:"M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z",fill:"currentColor"},null,-1),K=[F,J],O={class:"relative inline-flex items-center mb-5 cursor-pointer"},z=e("div",{class:"w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:w-5 after:h-5 after:transition-all peer-checked:bg-blue-600"},null,-1),G=e("span",{class:"ms-3 text-sm font-medium text-gray-900"},"Show pipline status",-1),Q={key:0,class:"p-2 text-red-600"},W=["src"],ee={__name:"PinMatchView",setup(X){const r=d({year:"2023",month:"1",db:"BE_SCRATCH",schm:"EARABMAKKI",s3:"mf-datascience",prefix:"ascend_pin_matching/transfer_data/new",flowSwitch:!0}),a=d({label:"Start Process",isLoading:!1}),c=d(""),g=d(!1);w(()=>{const n=sessionStorage.getItem("iframUrl");n!==null&&(c.value=n)}),C(c,n=>{sessionStorage.setItem("iframUrl",n)});const i=d(""),v=async()=>{const n="/proxy/8000/pinmatch";a.value.isLoading=!0,a.value.label="Loading...";try{console.log(r.value);const l=await M.post(n,r.value);i.value=l.data.message,c.value="https://metaflow.ml.bestegg.com/PLPinMatch/"+l.data.run_id}catch(l){i.value=l,console.error(l)}finally{a.value.isLoading=!1,a.value.label="Start Process"}},_=()=>{r.value.flowSwitch=!1,v(),r.value.flowSwitch=!0};return(n,l)=>(o(),s(x,null,[B,e("form",{onSubmit:V(v,["prevent"])},[e("div",A,[e("div",L,[e("div",null,[P,u(e("select",{id:"countries","onUpdate:modelValue":l[0]||(l[0]=t=>r.value.year=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 hover:cursor-pointer"},[(o(!0),s(x,null,y(Array.from({length:11},(t,p)=>2023-p),t=>(o(),s("option",{value:t},f(t),9,E))),256))],512),[[h,r.value.year]])]),e("div",null,[q,u(e("select",{id:"countries","onUpdate:modelValue":l[1]||(l[1]=t=>r.value.month=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 hover:cursor-pointer"},[(o(!0),s(x,null,y(Array.from({length:11},(t,p)=>11-p),t=>(o(),s("option",{value:t},f(t),9,D))),256))],512),[[h,r.value.month]])]),e("div",null,[N,u(e("input",{type:"text","onUpdate:modelValue":l[2]||(l[2]=t=>r.value.db=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",placeholder:"BE_SCRATCH",required:""},null,512),[[b,r.value.db]])]),e("div",null,[T,u(e("input",{type:"text","onUpdate:modelValue":l[3]||(l[3]=t=>r.value.schm=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",placeholder:"DJOHN",required:""},null,512),[[b,r.value.schm]])]),e("div",null,[H,u(e("input",{type:"text","onUpdate:modelValue":l[4]||(l[4]=t=>r.value.s3=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",required:""},null,512),[[b,r.value.s3]])]),e("div",null,[I,u(e("input",{type:"text","onUpdate:modelValue":l[5]||(l[5]=t=>r.value.prefix=t),class:"bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",required:""},null,512),[[b,r.value.prefix]])])]),e("div",R,[e("div",null,[e("button",{disabled:a.value.isLoading,type:"submit",class:"m-1 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 inline-flex items-center"},[a.value.isLoading?(o(),s("svg",j,K)):m("",!0),k(),e("span",null,f(a.value.label),1)],8,Z),i.value?(o(),s("button",{key:0,type:"button",onClick:_,class:"text-red-700 px-5 py-2.5 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm text-center me-2"}," Stop process ")):m("",!0)]),e("label",O,[u(e("input",{type:"checkbox","onUpdate:modelValue":l[6]||(l[6]=t=>g.value=t),class:"sr-only peer"},null,512),[[S,g.value]]),z,G])])])],40,U),i.value?(o(),s("div",Q,f(i.value),1)):m("",!0),e("div",null,[g.value?(o(),s("iframe",{key:0,src:c.value,class:"w-full min-h-screen",frameborder:"1"},null,8,W)):m("",!0)])],64))}};export{ee as default};
