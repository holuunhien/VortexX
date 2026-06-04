// ==UserScript==
// @name          Cytos Screen Rainbow (v8.0 Global CSS Filter)
// @namespace     https://violentmonkey.net/
// @version       8.0
// @description   Ép toàn bộ khung game xoay màu cầu vồng trực tiếp từ trình duyệt. Không sợ WebGL, 100% không lag phím.
// @author        HLN Engine
// @match         https://cytos.io/*
// @match         https://*.cytos.io/*
// @icon          https://github.com/holuunhien/VortexX/blob/main/colorful.js
// @license       MIT
// @grant         none
// @run-at        document-end
// ==/UserScript==

(function() {
    'use strict';

    // 1. Chèn hiệu ứng CSS xoay dải màu vào trang web
    const style = document.createElement('style');
    style.type = 'text/css';
    style.innerHTML = `
        @keyframes globalRainbow {
            0%   { filter: hue-rotate(0deg) saturate(120%); }
            100% { filter: hue-rotate(360deg) saturate(120%); }
        }

        /* Ép hiệu ứng lên TẤT CẢ các thẻ Canvas (Khung chơi game) xuất hiện trên Cytos */
        canvas {
            animation: globalRainbow 6s linear infinite !important;
        }
    `;
    document.head.appendChild(style);

    console.log("Cytos v8.0 Global CSS Filter đã kích hoạt thành công!");
})();
