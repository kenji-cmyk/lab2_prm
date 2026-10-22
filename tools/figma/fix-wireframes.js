const p=await figma.getNodeByIdAsync('2:2');await figma.setCurrentPageAsync(p);
const oldIds=['12:4','12:12','12:22','12:32','12:41','12:49','12:58','12:65','12:74','12:82','12:96'];
const keepIds=['52:407','52:425','52:466','52:549','52:596','52:631','52:666','52:696','52:776','52:856','52:947'];
const labelIds=['12:5','12:13','12:23','12:33','12:42','12:50','12:59','12:66','12:75','12:83','12:97'];
const removed=[],mutated=[];for(const id of oldIds){const n=await figma.getNodeByIdAsync(id);if(n){n.remove();removed.push(id);}}
const texts=await Promise.all(['12:2',...labelIds].map(id=>figma.getNodeByIdAsync(id)));const fonts=new Map();for(const t of texts)for(const seg of t.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(seg.fontName),seg.fontName);await Promise.all([...fonts.values()].map(f=>figma.loadFontAsync(f)));
for(let i=0;i<keepIds.length;i++){const f=await figma.getNodeByIdAsync(keepIds[i]);f.x=40+(i%3)*420;f.y=180+Math.floor(i/3)*900;const l=texts[i+1];l.x=f.x;l.y=f.y-32;l.characters=f.name.replace('WF — ','');mutated.push(f.id,l.id);}
texts[0].characters='02 Wireframe · Bố cục low-fi';mutated.push(texts[0].id);
let note=p.children.find(n=>n.name==='Wireframe provenance');const created=[];if(!note){note=figma.createText();note.name='Wireframe provenance';note.fontName={family:'Roboto',style:'Regular'};await figma.loadFontAsync(note.fontName);note.fontSize=14;note.lineHeight={unit:'PIXELS',value:20};note.characters='Bộ đối chiếu dựng hồi cứu từ Final UI ngày 22/10/2026. Không phải bằng chứng wireframe trước AI generation.';note.resize(1200,40);note.textAutoResize='HEIGHT';note.x=40;note.y=84;created.push(note.id);}
return {createdNodeIds:created,mutatedNodeIds:mutated,removedNodeIds:removed,frames:p.children.filter(n=>n.type==='FRAME').map(n=>({id:n.id,name:n.name,x:n.x,y:n.y,width:n.width,height:n.height}))};
