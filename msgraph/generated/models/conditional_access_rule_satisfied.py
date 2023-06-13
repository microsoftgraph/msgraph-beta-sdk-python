from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_conditions, conditional_access_rule

@dataclass
class ConditionalAccessRuleSatisfied(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Refers to the conditional access policy conditions that are satisfied. The possible values are: none, application, users, devicePlatform, location, clientType, signInRisk, userRisk, time, deviceState, client, ipAddressSeenByAzureAD, ipAddressSeenByResourceProvider, unknownFutureValue, servicePrincipals, servicePrincipalRisk. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: servicePrincipals, servicePrincipalRisk.
    conditional_access_condition: Optional[conditional_access_conditions.ConditionalAccessConditions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Refers to the conditional access policy conditions that were satisfied. The possible values are: allApps, firstPartyApps, office365, appId, acr, appFilter, allUsers, guest, groupId, roleId, userId, allDevicePlatforms, devicePlatform, allLocations, insideCorpnet, allTrustedLocations, locationId, allDevices, deviceFilter, deviceState, unknownFutureValue, deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider, microsoftAdminPortals. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: deviceFilterIncludeRuleNotMatched, allDeviceStates, anonymizedIPAddress, unfamiliarFeatures, nationStateIPAddress, realTimeThreatIntelligence, internalGuest, b2bCollaborationGuest, b2bCollaborationMember, b2bDirectConnectUser, otherExternalUser, serviceProvider, microsoftAdminPortals.
    rule_satisfied: Optional[conditional_access_rule.ConditionalAccessRule] = None
    
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
        from . import conditional_access_conditions, conditional_access_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "conditionalAccessCondition": lambda n : setattr(self, 'conditional_access_condition', n.get_enum_value(conditional_access_conditions.ConditionalAccessConditions)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleSatisfied": lambda n : setattr(self, 'rule_satisfied', n.get_enum_value(conditional_access_rule.ConditionalAccessRule)),
        }
        return fields
    
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
    

