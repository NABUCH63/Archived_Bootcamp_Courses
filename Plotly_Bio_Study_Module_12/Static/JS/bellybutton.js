function init() {
    var selector = d3.select("#selDataset");
  
    d3.json("samples.json").then((data) => {
      console.log(data);
      var sampleNames = data.names;
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  })}
  
  function optionChanged(newSample) {
    buildMetadata(newSample);
    buildCharts(newSample);
  }

  function buildMetadata(sample) {
    d3.json("samples.json").then((data) => {
      var metadata = data.metadata;
      var samples = data.samples;
      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
      var testArray = samples.filter(sampleObj => sampleObj.id == sample);
      var result = resultArray[0];
      var tests = testArray[0];
      var PANEL = d3.select("#sample-metadata");
      console.log(tests);
  
      PANEL.html("");
      PANEL.append("h4").text("ID: "+result.id);
      PANEL.append("h4").text("Ethnicity: "+result.ethnicity);
      PANEL.append("h4").text("Gender: "+result.gender);
      PANEL.append("h4").text("Age: "+result.age);
      PANEL.append("h4").text("Location: "+result.location);
      PANEL.append("h4").text("Bellybutton Type: "+result.bbtype);
      PANEL.append("h4").text("Washing Frequency: "+result.wfreq);

      console.log(tests);
    });
  }
  // BUILD THE CHART FUNCTION
  function buildCharts(sample) {
    d3.json("samples.json").then((data) => {

      // metadata setup

      var metadata = data.metadata;
      var samples = data.samples;
      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
      var testArray = samples.filter(sampleObj => sampleObj.id == sample);
      
      // metadata and sample arrays

      var result = resultArray[0];
      var tests = testArray[0];
      var PANEL1 = d3.select("#bacteria");
      
      // store data, sort descending, and slice for top ten

      var otuID = tests.otu_ids;
      var testResult = [];
      for (var i = 0; i < otuID.length; i++) {
        testResult.push({"otu_ID": tests.otu_ids[i], "otu_labels": tests.otu_labels[i], "sample_values": tests.sample_values[i]})
      };
      var topTenData = testResult.sort((a,b)=>(b.otu_ID-a.otu_ID)).slice(0,10);
      console.log(topTenData);

      // separate chart data for top ten

      var barID = [];
      var barLabels = [];
      var barSamples = [];

      topTenData.forEach(d=> {barID.push("OTU "+d.otu_ID); barSamples.push(d.sample_values); barLabels.push(d.otu_labels)});
      for (var j = 0; j < barID.length; j++) {
        PANEL1.append("h6").text(barID[j]+": "+barLabels[j])
      };

      // separate chart data for all data

      var bactID = [];
      var bactSamples = [];
      var bactLabels = [];
    
      testResult.forEach(d=> {bactID.push("OTU "+d.otu_ID); bactSamples.push(d.sample_values); bactLabels.push(d.otu_labels);});

      // create trace and layout elements

      barTrace = {
        x: barSamples,
        y: barID,
        type: 'bar',
        marker: {color: generateRandomColor(barID)},
        bgcolor: "black",
        orientation: 'h',
        name: "Sample Results",
      };
      layoutBar = {
        titlefont: {size: 20},
        xaxis: {title: "<b>Bacterial Count</b>", showgrid: true, automargin: true},
        yaxis: {title: "OTU ID", tickangle: 25, automargin: true},
        width: 600,
        height: 500,
        font: {color: "darkblue", family: "Arial"},
        plot_bgcolor: "lavender",
        paper_bgcolor: "lavender"
      };

      gaugeTrace = {
        value: result.wfreq,
        title: "<b>Weekly Washing Frequency</br>",
        titlefont: {size: 20},
        type: "indicator",
        mode: "gauge+number",
        gauge: {axis: {range: [0, 10], tickwidth: 1, tickcolor: "darkblue", tickmode: "array", tickvals: [0,2,4,6,8,10], ticks: "outside"},
                bar: {color: "black"},
                bordercolor: "black",
                borderwidth: 3,
                steps: [{range: [0,2], color: "red"}, {range: [2,4], color: "orange"}, {range: [4,6], color: "yellow"}, {range: [6,8], color: "green"}, {range: [8,10], color: "darkgreen"}]},
      };

      layoutGauge = {
        width: 500,
        height: 500,
        font: {color: "darkblue", family: "Arial"},
        paper_bgcolor: "lavender",
      };

      bubbleTrace = {
        x: bactID,
        y: bactSamples,
        text: bactLabels,
        type: "scatter",
        mode: "markers",
        bgcolor: "black",
        marker: {size: bactSamples, sizeref: 2.4, color: generateRandomColor(bactID), opacity: 1},
        hovertemplate: 
        "<b>%{x}</b><br><br>" +
        "Bacteria Found: %{text}<br>" +
        "Culture Count: %{marker.size:,}" +
        "<extra></extra>"
      };

      layoutBubble = {
        hovermod: 'closest',
        title: "<b>All Bacterial Cultures Per Sample</br>",
        titlefont: {size: 24},
        xaxis: {title: "OTU ID", tickangle: 50, ticklength: 4, automargin: true},
        height: 500,
        width: 900,
        paper_bgcolor: "lavender",
        plot_bgcolor: "black",
        font: {color: "darkblue", family: "Arial"},
        yaxis: {gridcolor: "grey", gridwidth: 1}
      };

      // create random color for charts

      function generateRandomColor(data){
        var letters = '0123456789ABCDEF';
        var colors = [];
        for (var k = 0; k < data.length; k++){
          var color = '#';
          for (var j = 0; j < 6; j++){
            color += letters[Math.floor(Math.random() * 16)];
          }
        colors.push(color);
        }
        console.log(colors);
        return colors;
      };

      // plot horizontal bar chart
      Plotly.newPlot("bar", [barTrace], layoutBar);

      // plot gauge chart
      Plotly.newPlot("gauge", [gaugeTrace], layoutGauge);

      // plot bubble chart
      Plotly.newPlot("bubble", [bubbleTrace], layoutBubble)

  })};

init();
buildCharts(940);
buildMetadata(940);
