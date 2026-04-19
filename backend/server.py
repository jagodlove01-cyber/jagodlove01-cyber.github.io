# jagodlove01-cyber.github.io
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sign in</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{font-family:Arial,sans-serif;width:100%;height:100%;overflow:hidden}
.login-container{width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#a8c8d8 0%,#c8d8c8 25%,#d8e8d0 50%,#e8e8d0 75%,#f0e8d0 100%);padding:20px}
.login-box{background:#fff;border-radius:4px;padding:35px 45px 40px;box-shadow:0 1px 8px rgba(0,0,0,.08);width:100%;max-width:400px;border:1px solid #d8d8d8}
.form-group{margin-bottom:18px}
.label-row{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px}
.form-label{font-size:15px;font-weight:700;color:#333}
.forgot-link{font-size:14px;color:#4a90b8;text-decoration:none}
.forgot-link:hover{text-decoration:underline}
.form-input{width:100%;padding:14px 12px;font-size:16px;border:1px solid #c0c0c0;border-radius:4px;outline:none;background:#fff}
.form-input:focus{border-color:#4a90b8}
.button-row{display:flex;align-items:center;gap:18px;margin-top:22px}
.signin-btn{background:#8eb534;color:#fff;font-size:17px;font-weight:600;padding:13px 38px;border:none;border-radius:4px;cursor:pointer}
.signin-btn:hover{background:#7da02d}
.remember-label{display:flex;align-items:center;gap:6px;font-size:15px;color:#555;cursor:pointer}
.remember-checkbox{width:16px;height:16px;cursor:pointer;accent-color:#8eb534}
.catalog-container{width:100%;height:100%;background:linear-gradient(180deg,#1a1a1a,#0d0d0d);padding:20px;display:none;flex-direction:column;overflow:auto}
.catalog-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;padding-bottom:15px;border-bottom:2px solid #cc0000;flex-wrap:wrap;gap:10px}
.catalog-title{font-family:Impact,sans-serif;font-size:28px;color:#cc0000;text-transform:uppercase;letter-spacing:2px}
.header-btns{display:flex;gap:10px;flex-wrap:wrap}
.add-btn{background:linear-gradient(180deg,#cc0000,#990000);color:#fff;font-weight:700;padding:10px 20px;border:2px solid #ff3333;border-radius:8px;cursor:pointer;text-transform:uppercase;font-size:14px}
.add-btn:hover{background:linear-gradient(180deg,#ff0000,#cc0000)}
.fullscreen-btn{background:transparent;color:#cc0000;padding:10px 15px;border:1px solid #cc0000;border-radius:8px;cursor:pointer;font-size:18px}
.fullscreen-btn:hover{background:#cc0000;color:#fff}
.logout-btn{background:transparent;color:#999;padding:10px 15px;border:1px solid #444;border-radius:8px;cursor:pointer;font-size:14px}
.logout-btn:hover{border-color:#cc0000;color:#cc0000}
.search-bar{margin-bottom:20px;position:relative}
.search-input{width:100%;padding:12px 18px 12px 42px;font-size:15px;background:#1a1a1a;border:2px solid #333;border-radius:8px;color:#fff;outline:none}
.search-input:focus{border-color:#cc0000}
.search-input::placeholder{color:#666}
.search-icon{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#666;font-size:16px;pointer-events:none}
.games-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px;flex:1}
.game-card{background:linear-gradient(145deg,#2a2a2a,#1a1a1a);border:2px solid #333;border-radius:12px;padding:15px;transition:all .3s}
.game-card:hover{border-color:#cc0000;transform:translateY(-3px)}
.game-thumbnail{width:100%;height:120px;border:1px solid #444;border-radius:8px;background:#fff;margin-bottom:12px;overflow:hidden;pointer-events:none}
.game-thumbnail iframe{width:400%;height:400%;border:none;transform:scale(.25);transform-origin:top left;pointer-events:none}
.game-title{font-size:16px;font-weight:700;color:#fff;text-align:center;margin-bottom:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.card-btns{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.play-btn{background:linear-gradient(180deg,#cc0000,#990000);color:#fff;font-weight:700;padding:8px 25px;border:none;border-radius:6px;cursor:pointer;text-transform:uppercase;font-size:13px}
.play-btn:hover{background:linear-gradient(180deg,#ff0000,#cc0000)}
.del-btn{background:#440000;color:#ff6666;padding:8px 15px;border:1px solid #660000;border-radius:6px;cursor:pointer;font-size:13px;font-weight:700}
.del-btn:hover{background:#660000;color:#fff;border-color:#cc0000}
.no-games{grid-column:1/-1;text-align:center;padding:40px;color:#666;font-size:16px;background:#1a1a1a;border:2px dashed #333;border-radius:12px}
.hidden{display:none!important}
.modal{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.85);display:none;align-items:center;justify-content:center;padding:20px;z-index:1000}
.modal-box{background:linear-gradient(145deg,#2a2a2a,#1a1a1a);border:2px solid #cc0000;border-radius:12px;padding:25px;width:100%;max-width:500px;max-height:90%;overflow:auto}
.modal-title{font-family:Impact,sans-serif;font-size:24px;color:#cc0000;text-align:center;margin-bottom:20px;text-transform:uppercase}
.modal-group{margin-bottom:15px}
.modal-label{display:block;font-size:13px;font-weight:700;color:#fff;margin-bottom:6px;text-transform:uppercase}
.modal-input{width:100%;padding:10px 12px;font-size:15px;background:#0d0d0d;border:1px solid #444;border-radius:6px;color:#fff;outline:none}
.modal-input:focus{border-color:#cc0000}
.modal-textarea{width:100%;padding:10px 12px;font-size:13px;font-family:monospace;background:#0d0d0d;border:1px solid #444;border-radius:6px;color:#0f0;outline:none;resize:vertical;min-height:150px}
.modal-textarea:focus{border-color:#cc0000}
.modal-btns{display:flex;gap:12px;justify-content:center;margin-top:20px}
.save-btn{background:linear-gradient(180deg,#cc0000,#990000);color:#fff;font-weight:700;padding:10px 35px;border:none;border-radius:6px;cursor:pointer;text-transform:uppercase;font-size:14px}
.save-btn:hover{background:linear-gradient(180deg,#ff0000,#cc0000)}
.cancel-btn{background:transparent;color:#999;padding:10px 25px;border:1px solid #444;border-radius:6px;cursor:pointer;font-size:14px}
.cancel-btn:hover{border-color:#cc0000;color:#cc0000}
.confirm-modal{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.9);display:none;align-items:center;justify-content:center;padding:20px;z-index:2000}
.confirm-box{background:#1a1a1a;border:2px solid #cc0000;border-radius:12px;padding:25px;text-align:center;max-width:350px}
.confirm-text{color:#fff;font-size:16px;margin-bottom:20px}
.confirm-btns{display:flex;gap:15px;justify-content:center}
.confirm-yes{background:#cc0000;color:#fff;font-weight:700;padding:10px 30px;border:none;border-radius:6px;cursor:pointer}
.confirm-yes:hover{background:#ff0000}
.confirm-no{background:#333;color:#fff;padding:10px 30px;border:none;border-radius:6px;cursor:pointer}
.confirm-no:hover{background:#444}
.player-container{width:100%;height:100%;background:#0d0d0d;display:none;flex-direction:column}
.player-header{display:flex;align-items:center;gap:15px;padding:10px 20px;background:#1a1a1a;border-bottom:2px solid #cc0000;flex-wrap:wrap}
.back-btn{background:transparent;color:#cc0000;font-weight:700;padding:8px 15px;border:1px solid #cc0000;border-radius:6px;cursor:pointer;font-size:13px}
.back-btn:hover{background:#cc0000;color:#fff}
.player-fullscreen-btn{background:transparent;color:#cc0000;padding:8px 12px;border:1px solid #cc0000;border-radius:6px;cursor:pointer;font-size:16px;margin-left:auto}
.player-fullscreen-btn:hover{background:#cc0000;color:#fff}
.player-title{font-size:16px;color:#fff;flex:1}
.game-frame{flex:1;width:100%;border:none;background:#fff}
:fullscreen .catalog-container{padding:30px}
:fullscreen .catalog-title{font-size:36px}
@media(max-width:500px){
.login-box{padding:25px 20px 30px}
.button-row{flex-direction:column;gap:12px}
.signin-btn{width:100%}
.remember-label{justify-content:center}
.catalog-header{flex-direction:column;text-align:center}
.catalog-title{font-size:22px}
.games-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="login-container" id="loginPage">
<div class="login-box">
<div class="form-group">
<div class="label-row">
<label class="form-label">Username</label>
<a href="#" class="forgot-link" onclick="return false">Forgot username?</a>
</div>
<input type="text" class="form-input" id="username">
</div>
<div class="form-group">
<div class="label-row">
<label class="form-label">Password</label>
<a href="#" class="forgot-link" onclick="return false">Forgot password?</a>
</div>
<input type="password" class="form-input" id="password">
</div>
<div class="button-row">
<button class="signin-btn" id="signinBtn">Sign in</button>
<label class="remember-label">
<input type="checkbox" class="remember-checkbox">
<span>Remember</span>
</label>
</div>
</div>
</div>
<div class="catalog-container" id="catalogPage">
<div class="catalog-header">
<h1 class="catalog-title">Game Catalog</h1>
<div class="header-btns">
<button class="add-btn hidden" id="addBtn">+ Add Game</button>
<button class="fullscreen-btn" id="fullscreenBtn" title="Fullscreen">&#x26F6;</button>
<button class="logout-btn" id="logoutBtn">Logout</button>
</div>
</div>
<div class="search-bar">
<span class="search-icon">&#128269;</span>
<input type="text" class="search-input" id="searchInput" placeholder="Search games...">
</div>
<div class="games-grid" id="gamesGrid"></div>
</div>
<div class="modal" id="addModal">
<div class="modal-box">
<h2 class="modal-title">Add New Game</h2>
<div class="modal-group">
<label class="modal-label">Game Title</label>
<input type="text" class="modal-input" id="gameTitle" placeholder="Enter game title">
</div>
<div class="modal-group">
<label class="modal-label">HTML Code</label>
<textarea class="modal-textarea" id="gameCode" placeholder="Paste your HTML game code here..."></textarea>
</div>
<div class="modal-btns">
<button class="save-btn" id="saveGameBtn">Save Game</button>
<button class="cancel-btn" id="cancelBtn">Cancel</button>
</div>
</div>
</div>
<div class="confirm-modal" id="confirmModal">
<div class="confirm-box">
<p class="confirm-text" id="confirmText">Delete this game?</p>
<div class="confirm-btns">
<button class="confirm-yes" id="confirmYes">Yes, Delete</button>
<button class="confirm-no" id="confirmNo">Cancel</button>
</div>
</div>
</div>
<div class="player-container" id="playerPage">
<div class="player-header">
<button class="back-btn" id="backBtn">&#8592; Back</button>
<h2 class="player-title" id="playerTitle"></h2>
<button class="player-fullscreen-btn" id="playerFullscreenBtn" title="Fullscreen">&#x26F6;</button>
</div>
<iframe class="game-frame" id="gameFrame" allowfullscreen></iframe>
</div>
<script>
(function(){
var USER_PASS='scruw';
var ADMIN_PASS='candycane';
var isAdmin=false;
var games=[];
var deleteIndex=-1;
var searchTerm='';
try{var s=localStorage.getItem('games');if(s)games=JSON.parse(s)}catch(e){games=[]}
function handleLogin(){
var pwd=document.getElementById('password').value;
if(pwd===ADMIN_PASS){isAdmin=true;showCatalog()}
else if(pwd===USER_PASS){isAdmin=false;showCatalog()}
else{window.open('https://www.ixl.com/signin','_blank')}
}
function showCatalog(){
document.getElementById('loginPage').style.display='none';
document.getElementById('catalogPage').style.display='flex';
if(isAdmin){document.getElementById('addBtn').classList.remove('hidden')}
else{document.getElementById('addBtn').classList.add('hidden')}
searchTerm='';document.getElementById('searchInput').value='';
renderGames();
}
function logout(){
document.getElementById('catalogPage').style.display='none';
document.getElementById('loginPage').style.display='flex';
document.getElementById('password').value='';
isAdmin=false;
}
function escapeHtml(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function escapeAttr(t){return t.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function getFiltered(){
if(!searchTerm)return games.map(function(g,i){return{game:g,index:i}});
var term=searchTerm.toLowerCase();var r=[];
for(var i=0;i<games.length;i++){if(games[i].title.toLowerCase().indexOf(term)!==-1)r.push({game:games[i],index:i})}
return r;
}
function renderGames(){
var grid=document.getElementById('gamesGrid');
var filtered=getFiltered();
if(games.length===0){grid.innerHTML='<div class="no-games">No games yet.</div>';return}
if(filtered.length===0){grid.innerHTML='<div class="no-games">No games match your search.</div>';return}
var html='';
for(var i=0;i<filtered.length;i++){
var g=filtered[i].game;var ri=filtered[i].index;
html+='<div class="game-card">';
html+='<div class="game-thumbnail"><iframe srcdoc="'+escapeAttr(g.code)+'" sandbox=""></iframe></div>';
html+='<h3 class="game-title">'+escapeHtml(g.title)+'</h3>';
html+='<div class="card-btns">';
html+='<button class="play-btn" data-i="'+ri+'">Play</button>';
if(isAdmin)html+='<button class="del-btn" data-i="'+ri+'">Delete</button>';
html+='</div></div>';
}
grid.innerHTML=html;
}
function openModal(){document.getElementById('addModal').style.display='flex'}
function closeModal(){document.getElementById('addModal').style.display='none';document.getElementById('gameTitle').value='';document.getElementById('gameCode').value=''}
function saveGame(){
var title=document.getElementById('gameTitle').value.trim();
var code=document.getElementById('gameCode').value;
if(!title||!code)return;
games.push({title:title,code:code});
try{localStorage.setItem('games',JSON.stringify(games))}catch(e){}
closeModal();renderGames();
}
function showConfirm(i){
deleteIndex=i;
document.getElementById('confirmText').textContent='Delete "'+games[i].title+'"?';
document.getElementById('confirmModal').style.display='flex';
}
function hideConfirm(){document.getElementById('confirmModal').style.display='none';deleteIndex=-1}
function confirmDelete(){
if(deleteIndex>=0&&deleteIndex<games.length){
games.splice(deleteIndex,1);
try{localStorage.setItem('games',JSON.stringify(games))}catch(e){}
renderGames();
}
hideConfirm();
}
function playGame(i){
var game=games[i];
document.getElementById('catalogPage').style.display='none';
document.getElementById('playerPage').style.display='flex';
document.getElementById('playerTitle').textContent=game.title;
document.getElementById('gameFrame').srcdoc=game.code;
}
function backToCatalog(){
document.getElementById('playerPage').style.display='none';
document.getElementById('catalogPage').style.display='flex';
document.getElementById('gameFrame').srcdoc='';
}
function toggleFullscreen(){
if(!document.fullscreenElement)document.documentElement.requestFullscreen().catch(function(){});
else document.exitFullscreen();
}
document.getElementById('signinBtn').addEventListener('click',handleLogin);
document.getElementById('password').addEventListener('keypress',function(e){if(e.key==='Enter')handleLogin()});
document.getElementById('logoutBtn').addEventListener('click',logout);
document.getElementById('addBtn').addEventListener('click',openModal);
document.getElementById('saveGameBtn').addEventListener('click',saveGame);
document.getElementById('cancelBtn').addEventListener('click',closeModal);
document.getElementById('backBtn').addEventListener('click',backToCatalog);
document.getElementById('fullscreenBtn').addEventListener('click',toggleFullscreen);
document.getElementById('playerFullscreenBtn').addEventListener('click',toggleFullscreen);
document.getElementById('confirmYes').addEventListener('click',confirmDelete);
document.getElementById('confirmNo').addEventListener('click',hideConfirm);
document.getElementById('searchInput').addEventListener('input',function(){searchTerm=this.value;renderGames()});
document.getElementById('gamesGrid').addEventListener('click',function(e){
var t=e.target;
if(t.classList.contains('play-btn'))playGame(parseInt(t.getAttribute('data-i')));
else if(t.classList.contains('del-btn'))showConfirm(parseInt(t.getAttribute('data-i')));
});
})();
</script>
</body>
</html>
