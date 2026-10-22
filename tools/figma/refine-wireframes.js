// Run through Figma MCP use_figma; scope: page 02 Wireframe only.
const p = await figma.getNodeByIdAsync('2:2');
await figma.setCurrentPageAsync(p);
const ids = ['52:407','52:425','52:466','52:549','52:596','52:631','52:666','52:696','52:776','52:856','52:947'];
const frames = await Promise.all(ids.map(id => figma.getNodeByIdAsync(id)));
if (frames.some(f => !f || f.parent.id !== p.id)) throw new Error('Wireframe inventory changed; inspect before retry.');
const all = frames.flatMap(f => [f, ...f.findAll(() => true)]);
const fontMap = new Map();
for (const t of all.filter(n => n.type === 'TEXT'))
  for (const seg of t.getStyledTextSegments(['fontName'])) fontMap.set(JSON.stringify(seg.fontName), seg.fontName);
await Promise.all([...fontMap.values()].map(f => figma.loadFontAsync(f)));
await figma.loadFontAsync({family:'Roboto',style:'Regular'});
const mutated = new Set(), created = [], removed = [];
const paint = v => [{type:'SOLID',color:{r:v,g:v,b:v}}];
const mark = n => {mutated.add(n.id);return n;};
const get = async id => {const n = await figma.getNodeByIdAsync(id);if(!n) throw new Error('Missing '+id);return mark(n);};
for (const n of all) {
  mark(n);
  if ('effects' in n) n.effects = [];
  if ('cornerRadius' in n) n.cornerRadius = 2;
  if (n.type === 'TEXT') {
    n.fills = paint(0.18);
    if (typeof n.fontSize === 'number' && n.fontSize > 24) n.fontSize = 24;
  } else if (n.type === 'FRAME') {
    if (ids.includes(n.id)) {
      n.fills = paint(1);n.strokes = paint(0.35);n.strokeWeight = 1;n.cornerRadius = 0;
    } else if (n.name === 'Button') {
      n.fills = paint(0.9);n.strokes = paint(0.25);n.strokeWeight = 2;
      for (const t of n.children.filter(c => c.type === 'TEXT')) t.fills = paint(0.12);
    } else if (['Card','Loading','Empty State','Error & Recovery','Input container'].includes(n.name)) {
      n.fills = paint(1);n.strokes = paint(0.55);n.strokeWeight = 1;
    } else if (n.name === 'App Bar') {
      n.fills = paint(0.96);n.strokes = [];
    } else if (['Leading action','Brand mark','Status icon'].includes(n.name)) {
      n.fills = [];n.strokes = [];
    }
  }
}
const hero = await get('52:412');
for (const c of [...hero.children]) {removed.push(c.id,...('findAll' in c?c.findAll(()=>true).map(d=>d.id):[]));c.remove();}
hero.resize(320,184);hero.layoutMode='VERTICAL';hero.primaryAxisSizingMode='FIXED';hero.counterAxisSizingMode='FIXED';hero.primaryAxisAlignItems='CENTER';hero.counterAxisAlignItems='CENTER';hero.fills=paint(0.96);hero.strokes=paint(0.55);hero.strokeWeight=1;hero.dashPattern=[6,4];hero.name='Illustration placeholder';
const imageLabel=figma.createText();imageLabel.fontName={family:'Roboto',style:'Regular'};imageLabel.fontSize=16;imageLabel.lineHeight={unit:'PIXELS',value:24};imageLabel.characters='[ Hình minh họa ]';imageLabel.fills=paint(0.3);hero.appendChild(imageLabel);created.push(imageLabel.id);
const headline=await get('52:418');headline.y=340;headline.resize(320,68);headline.lineHeight={unit:'PIXELS',value:32};
const welcomeBody=await get('52:419');welcomeBody.y=424;welcomeBody.resize(320,100);
for (const n of frames.flatMap(f=>f.findAll(n=>n.type==='FRAME'&&n.name==='Navigation Item'))) {
  const icon=n.children.find(c=>c.name==='Icon'),label=n.children.find(c=>c.name==='Label');
  if (!icon||!label) throw new Error('Unexpected nav structure: '+n.id);
  const selected=n.fills.some(f=>f.type==='SOLID'&&f.color.r<0.98);
  n.insertChild(0,icon);n.insertChild(1,label);
  n.layoutMode='VERTICAL';n.primaryAxisSizingMode='FIXED';n.counterAxisSizingMode='FIXED';
  n.primaryAxisAlignItems='CENTER';n.counterAxisAlignItems='CENTER';n.itemSpacing=4;
  n.paddingTop=4;n.paddingBottom=4;n.paddingLeft=0;n.paddingRight=0;
  icon.layoutPositioning='AUTO';label.layoutPositioning='AUTO';
  n.fills=paint(selected?0.94:1);n.strokes=paint(selected?0.25:0.75);n.strokeWeight=selected?2:1;
  label.textAlignHorizontal='CENTER';label.resize(82,20);
  for(const t of n.children.filter(c=>c.name==='Glyph')) t.visible=false;
  mark(icon);mark(label);
}
const setText = async (id, text, height) => {const n=await get(id);n.characters=text;if(height)n.resize(n.width,height);return n;};
await setText('52:456','✓ Thêm rau vào bữa ăn');
await setText('52:457','Đã chọn · Mục tiêu nhỏ cho hôm nay.');
const selected=await get('52:455');selected.fills=paint(0.96);selected.strokeWeight=2;selected.strokes=paint(0.25);
await setText('52:436','Có thể đổi lựa chọn trước khi lưu.',40);
await setText('52:670','Quay lại biểu mẫu để kiểm tra thông tin bữa ăn.',56);
await setText('52:779','Ngày chưa ghi bữa');
await setText('52:918','Bạn đã ghi nhận bữa ăn trong 5 ngày tuần này.',40);
function newText(parent,name,text,x,y,w,h,size=16){
  let n=parent.children.find(c=>c.name===name&&c.type==='TEXT');
  if(!n){n=figma.createText();parent.appendChild(n);created.push(n.id);}
  else mark(n);
  n.name=name;n.fontName={family:'Roboto',style:'Regular'};n.fontSize=size;
  n.lineHeight={unit:'PIXELS',value:size===14?20:24};n.characters=text;n.fills=paint(0.18);
  n.resize(w,h);n.x=x;n.y=y;return n;
}
newText(frames[4],'Result fallback link','Xem kết quả →',20,528,320,48);
newText(frames[7],'Empty day link','Xem ngày chưa ghi bữa →',20,574,320,48);
newText(frames[9],'Chart text alternative','Đã ghi: T2–T6 · Chưa ghi: T7, CN',20,426,320,20,14);
for(const id of ['52:863','52:865','52:867','52:869','52:871','52:873','52:875']){
  const bar=await get(id);bar.cornerRadius=0;bar.strokes=paint(0.3);bar.strokeWeight=1;
}
for (const f of frames) {
  // Reading order in this static wireframe follows vertical position.
  const ordered=[...f.children].sort((a,b)=>a.y-b.y||a.x-b.x);
  for(const child of ordered)f.appendChild(child);
}
const navChecks = frames.flatMap(f=>f.findAll(n=>n.type==='FRAME'&&n.name==='Navigation Item')).map(n=>{
  const icon=n.children.find(c=>c.name==='Icon'),label=n.children.find(c=>c.name==='Label');
  return {id:n.id,iconBottom:icon.y+icon.height,labelTop:label.y,gap:label.y-icon.y-icon.height};
});
return {createdNodeIds:created,mutatedNodeIds:[...mutated],removedNodeIds:removed,
  frameCount:frames.length,frames:frames.map(f=>({id:f.id,name:f.name,x:f.x,y:f.y,width:f.width,height:f.height})),
  navigationChecks:navChecks,fontFamilies:[...new Set(frames.flatMap(f=>f.findAllWithCriteria({types:['TEXT']})).map(t=>t.fontName.family))]};
