<p align="center">
  <img src="python/app_logo.png" alt="Comfortogether Logo" width="200"/>
</p>

# Team Comfortogether: Comfort + Togerther 

Video Recognition-based Application for the Visually Impaired

## Description

An offline application designed to assist visually impaired individuals with walking by using visual recognition to identify danger factors and tactile paving (Braille blocks) not recognized by a cane, providing sensory feedback (auditory and haptic).

## People

* Elim Kwak
* Jaewon Jeong
* Seoyeon Choi
* Seongmin Hwang

## Necessity and Problem Solving

### 1. Obstacles on Tactile Paving (PMs, Bicycles, Illegal Parking)
---
The increasing number of personal mobility device (PM) sharing services (e.g., kickboards and e-bikes) poses a threat to the passage of the visually impaired. While using a cane for mobility, they may find it difficult to identify distant objects or crowds due to the limited range of the cane. While bicycles are generally waist-high and easier to detect, electric kickboards are only ankle-height for adults, making them a significant tripping hazard even for sighted people.

* [cite_start]**Solution:** The system uses video analysis to provide immediate information about moving objects, preventing accidents caused by PMs, bicycles, and illegally parked vehicles on the walking path. [cite: 53, 180]

### 2. Solving Everyday Inconvenience: Wayfinding and Encroachment
---
According to the Anti-Corruption and Civil Rights Commission (ACRC), while visually impaired people experience difficulties with digital information, card usage, and purchasing medicine, **"wayfinding"** is the most challenging task. Between 2018 and 2020, 2,847 civil complaints were filed regarding tactile paving, including 603 cases concerning encroachment by illegally parked vehicles or other facilities.

* [cite_start]**Solution:** The application addresses the encroachment issue by detecting the lines formed by tactile paving and generating a **Braille block deviation warning (101)** if the user's detection area (B1, B2) moves outside these lines. [cite: 70, 290, 291]

### 3. Mitigating Guide Dog Costs and Requirements
---
The cost to train and provide one guide dog is approximately **₩100–200 million** (approx. \$75k–\$150k), involving about two years of training, with only 30–40% successfully becoming guide dogs. Additionally, obtaining a guide dog requires meeting strict conditions, such as having a daily destination, being employed, and having no children under 10 in the home. While some organizations provide guide dogs for free, the ongoing living expenses are the responsibility of the recipient.

* **Solution:** Comfortogether assists and partially substitutes the role of a guide dog, offering walking assistance without the heavy financial or stringent conditional burden.

## Development Environment and Tech Stack

* **GPU Environment:** RTX3060 TI (CUDA 11.8)
* **Collaboration tools:** ASANA, Github
* **Development Tools:** Visual Studio 2019, Jupyter Lab
* **Libraries & Frameworks:** OpenCV, **Pytorch**
* **Annotation Tools:** VIA

## Patent Filing Information (Technological Innovation)

[cite_start]The core technology of this project, the **"Walking Assistance System and Walking Assistance Method"**, has been filed with the Korean Intellectual Property Office (KIPO), confirming its innovative nature. [cite: 2, 39]

* [cite_start]**Application Number (출원번호):** 10-2023-0191701 [cite: 13]
* [cite_start]**Filing Date (출원일자):** December 26, 2023 [cite: 14]
* [cite_start]**Publication Number (공개번호):** 10-2025-0100280 [cite: 17]
* [cite_start]**Publication Date (공개일자):** July 3, 2025 [cite: 18]
* **Key Technical Features:**
    * [cite_start]**System Architecture:** Comprises a **Walking Assistance Device (110)** (with an Image Collection Module (111) and an Information Provision Module (113)) and an **Information Generation Unit (120)** utilizing multiple image analysis algorithms. [cite: 44, 45, 46, 49]
    * [cite_start]**Braille Block Recognition:** The system uses a specialized process: preprocess the front image to distinguish the tactile paving from the background [cite: 111] [cite_start]$\rightarrow$ recognize the lines formed by the tactile paving [cite: 112] [cite_start]$\rightarrow$ generate a deviation warning if the user's movement area leaves the recognized lines[cite: 113].
    * [cite_start]**Obstacle Detection:** It analyzes sequential image frames (comparing the 1st frame and the subsequent 2nd frame) to detect and classify obstacles (e.g., moving objects) using a Convolutional Neural Network (CNN) algorithm (121c), providing instantaneous warnings. [cite: 87, 338, 339, 340]
    * [cite_start]**Accurate Location:** It extracts text from structural signposts using **Bounding Boxes** and **Optical Character Recognition (OCR)**, compares this **Signpost Information** with **External Map DB** (via Open API), and generates accurate location information. [cite: 95, 96, 108]

## 📂 Folder Structure

```C
root
│  
├─android // Android App sources 
│     
└─python  // Image Processing sources 
│
<<<<<<< HEAD
└─ML  // Machine Learning sources
=======
└─ML  // Machine Learning sources
>>>>>>> bd836432fe8be884db675d1a31c6653000c135ab
