#!/usr/bin/env bash
set -xe

export REGION="us-east-1";
export AWS_CLI_PROFILE="default";
export CFN="cfn-cicd.yml";
export CFN_PARAM_JSON="cfn-cicd-param.json";
export APP_NAME="splayshapi-cicd";
export STACK_NAME="$APP_NAME";
export NOW=`date +%y%m%d%H%M%S`;

aws cloudformation validate-template \
--profile $AWS_CLI_PROFILE \
--template-body file://$CFN

# Check if the stack exists
if aws cloudformation describe-stacks \
--profile $AWS_CLI_PROFILE \
--stack-name "$STACK_NAME" \
--region "$REGION" \
>/dev/null 2>&1; then
    echo "Stack exists. Updating..."
    aws cloudformation update-stack \
    --stack-name "$STACK_NAME" \
    --template-body "file://$CFN" \
    --parameters "file://$CFN_PARAM_JSON" \
    --region "$REGION" \
    --capabilities CAPABILITY_IAM
    echo "Update initiated. Waiting for update to complete..."
    aws cloudformation wait stack-update-complete --stack-name "$STACK_NAME" --region "$REGION"
    echo "Stack update completed."
else
    echo "Stack doesn't exist. Creating..."
    aws cloudformation create-stack \
    --stack-name "$STACK_NAME" \
    --template-body "file://$CFN" \
    --parameters "file://$CFN_PARAM_JSON" \
    --region "$REGION" \
    --capabilities CAPABILITY_IAM
    echo "Creation initiated. Waiting for creation to complete..."
    aws cloudformation wait stack-create-complete --stack-name "$STACK_NAME" --region "$REGION"
    echo "Stack creation completed."
fi