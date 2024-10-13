---
layout: post
title:  "AquaMonitor"
date: 2024-10-13 16:54:00 +0900
categories: ESP32 ARDUINO PCB
author: VINI
tags: CECOM CAU
--- 



#### AquaMonitor 프로젝트 소개
**AquaMonitor**는 사용자가 음용수를 섭취할 때 발생하는 무게변화를 기반으로 음용수 섭취량을 측정하고 기록하는 서비스.
측정모듈과 텀블러, 코스터로 구성.
측정모듈을 각각 텀블러 하단부, 코스터 하단부에 붙여 사용할 수 있음.


#### 하드웨어
텀블러 하단부의 원형부분에 이질감없이 부착 가능하도록 FISION360을 활용하여 원형 PCB를 디자인하였으며, Uno에 사용되는 Atmega328p 칩과 APP과 BLE 통신을 위하여 HM-10 블루투스 통신 모듈을 부착하였음.

#### 어플리케이션
측정모듈과 BLE로 연결하여 사용할 수 있으며, 측정한 데이터를 편집하거나, 음료 종류 수정이 가능
설정한 음료 종류에 따라 수분의 함량을 고려하여 수분 섭취량에 반영.
구글의 헬스커넥트 API를 이용하였기에 기존 안드로이드 건강관리 어플리케이션에서도 업데이트된 수분 섭취량을 확인할 수 있음.
사용자의 연령, 성별, 수유여부에 따라 맞춤 수분 섭취 권장량이 업데이트 됨.


<p>
  <img src="/images/aquamonitor/1.jpg"  width="49%">
  <img src="/images/aquamonitor/2.jpg"  width="49%">
</p>
<p> 
  <img src="/images/aquamonitor/3.jpg"  width="49%">
  <img src="/images/aquamonitor/4.jpg"  width="49%">
</p>
<p>
  <img src="/images/aquamonitor/5.jpg"  width="49%">
  <img src="/images/aquamonitor/6.jpg"  width="49%">
</p>