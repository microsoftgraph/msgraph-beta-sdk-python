from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .administrative_unit_info import AdministrativeUnitInfo
    from .direct_routing_log_row import DirectRoutingLogRow
    from .pstn_call_log_row import PstnCallLogRow
    from .sms_log_row import SmsLogRow

@dataclass
class CallLogRow(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The administrativeUnitInfos property
    administrative_unit_infos: Optional[List[AdministrativeUnitInfo]] = None
    # The id property
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The otherPartyCountryCode property
    other_party_country_code: Optional[str] = None
    # The userDisplayName property
    user_display_name: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallLogRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.directRoutingLogRow".casefold():
            from .direct_routing_log_row import DirectRoutingLogRow

            return DirectRoutingLogRow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.pstnCallLogRow".casefold():
            from .pstn_call_log_row import PstnCallLogRow

            return PstnCallLogRow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.smsLogRow".casefold():
            from .sms_log_row import SmsLogRow

            return SmsLogRow()
        return CallLogRow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .administrative_unit_info import AdministrativeUnitInfo
        from .direct_routing_log_row import DirectRoutingLogRow
        from .pstn_call_log_row import PstnCallLogRow
        from .sms_log_row import SmsLogRow

        from .administrative_unit_info import AdministrativeUnitInfo
        from .direct_routing_log_row import DirectRoutingLogRow
        from .pstn_call_log_row import PstnCallLogRow
        from .sms_log_row import SmsLogRow

        fields: Dict[str, Callable[[Any], None]] = {
            "administrativeUnitInfos": lambda n : setattr(self, 'administrative_unit_infos', n.get_collection_of_object_values(AdministrativeUnitInfo)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "otherPartyCountryCode": lambda n : setattr(self, 'other_party_country_code', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("administrativeUnitInfos", self.administrative_unit_infos)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("otherPartyCountryCode", self.other_party_country_code)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

