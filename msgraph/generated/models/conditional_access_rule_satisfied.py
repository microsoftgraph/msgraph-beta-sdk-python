from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_conditions = lazy_import('msgraph.generated.models.conditional_access_conditions')
conditional_access_rule = lazy_import('msgraph.generated.models.conditional_access_rule')

class ConditionalAccessRuleSatisfied(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def conditional_access_condition(self,) -> Optional[conditional_access_conditions.ConditionalAccessConditions]:
        """
        Gets the conditionalAccessCondition property value. Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client, ipAddressSeenByAzureAD, ipAddressSeenByResourceProvider, unknownFutureValue, servicePrincipals, servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals, servicePrincipalRisk.
        Returns: Optional[conditional_access_conditions.ConditionalAccessConditions]
        """
        return self._conditional_access_condition
    
    @conditional_access_condition.setter
    def conditional_access_condition(self,value: Optional[conditional_access_conditions.ConditionalAccessConditions] = None) -> None:
        """
        Sets the conditionalAccessCondition property value. Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client, ipAddressSeenByAzureAD, ipAddressSeenByResourceProvider, unknownFutureValue, servicePrincipals, servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals, servicePrincipalRisk.
        Args:
            value: Value to set for the conditionalAccessCondition property.
        """
        self._conditional_access_condition = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessRuleSatisfied and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client, ipAddressSeenByAzureAD, ipAddressSeenByResourceProvider, unknownFutureValue, servicePrincipals, servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals, servicePrincipalRisk.
        self._conditional_access_condition: Optional[conditional_access_conditions.ConditionalAccessConditions] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Refers to the conditional access policy conditions that were satisfied. The possible values are: allApps, firstPartyApps, office365, appId, acr, appFilter, allUsers, guest, groupId, roleId, userId, allDevicePlatforms, devicePlatform, allLocations, insideCorpnet, allTrustedLocations, locationId, allDevices, deviceFilter, deviceState, unknownFutureValue, deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: deviceFilterIncludeRuleNotMatched, allDeviceStates.
        self._rule_satisfied: Optional[conditional_access_rule.ConditionalAccessRule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessRuleSatisfied:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessRuleSatisfied
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessRuleSatisfied()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conditional_access_condition": lambda n : setattr(self, 'conditional_access_condition', n.get_enum_value(conditional_access_conditions.ConditionalAccessConditions)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rule_satisfied": lambda n : setattr(self, 'rule_satisfied', n.get_enum_value(conditional_access_rule.ConditionalAccessRule)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def rule_satisfied(self,) -> Optional[conditional_access_rule.ConditionalAccessRule]:
        """
        Gets the ruleSatisfied property value. Refers to the conditional access policy conditions that were satisfied. The possible values are: allApps, firstPartyApps, office365, appId, acr, appFilter, allUsers, guest, groupId, roleId, userId, allDevicePlatforms, devicePlatform, allLocations, insideCorpnet, allTrustedLocations, locationId, allDevices, deviceFilter, deviceState, unknownFutureValue, deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: deviceFilterIncludeRuleNotMatched, allDeviceStates.
        Returns: Optional[conditional_access_rule.ConditionalAccessRule]
        """
        return self._rule_satisfied
    
    @rule_satisfied.setter
    def rule_satisfied(self,value: Optional[conditional_access_rule.ConditionalAccessRule] = None) -> None:
        """
        Sets the ruleSatisfied property value. Refers to the conditional access policy conditions that were satisfied. The possible values are: allApps, firstPartyApps, office365, appId, acr, appFilter, allUsers, guest, groupId, roleId, userId, allDevicePlatforms, devicePlatform, allLocations, insideCorpnet, allTrustedLocations, locationId, allDevices, deviceFilter, deviceState, unknownFutureValue, deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: deviceFilterIncludeRuleNotMatched, allDeviceStates.
        Args:
            value: Value to set for the ruleSatisfied property.
        """
        self._rule_satisfied = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("conditionalAccessCondition", self.conditional_access_condition)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleSatisfied", self.rule_satisfied)
        writer.write_additional_data_value(self.additional_data)
    

