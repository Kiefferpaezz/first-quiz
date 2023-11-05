package org.velezreyes.quiz.question6;

public class KarenTea implements Drink {

    private String name;
    private boolean isFizzy;
    private String response; 

    public KarenTea(String name, boolean isFizzy, String response) {
        this.name = name;
        this.isFizzy = isFizzy;
        this.response = response;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return isFizzy;
    }

    public String getResponse() {
        return response;
    }
}

