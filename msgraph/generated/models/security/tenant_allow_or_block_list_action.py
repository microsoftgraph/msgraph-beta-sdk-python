from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

tenant_allow_block_list_action = lazy_import('msgraph.generated.models.security.tenant_allow_block_list_action')
tenant_allow_block_list_entry_result = lazy_import('msgraph.generated.models.security.tenant_allow_block_list_entry_result')

class TenantAllowOrBlockListAction(AdditionalDataHolder, Parsable):
    @property
    def action(self,) -> Optional[tenant_allow_block_list_action.TenantAllowBlockListAction]:
        """
        Gets the action property value. Specifies whether the tenant allow block list is an allow or block. The possible values are: allow, block, and unkownFutureValue.
        Returns: Optional[tenant_allow_block_list_action.TenantAllowBlockListAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[tenant_allow_block_list_action.TenantAllowBlockListAction] = None) -> None:
        """
        Sets the action property value. Specifies whether the tenant allow block list is an allow or block. The possible values are: allow, block, and unkownFutureValue.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new tenantAllowOrBlockListAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether the tenant allow block list is an allow or block. The possible values are: allow, block, and unkownFutureValue.
        self._action: Optional[tenant_allow_block_list_action.TenantAllowBlockListAction] = None
        # Specifies when the tenant allow-block-list expires in date time.
        self._expiration_date_time: Optional[datetime] = None
        # Specifies the note added to the tenant allow block list entry in the format of string.
        self._note: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Contains the result of the submission that lead to the tenant allow-block-list entry creation.
        self._results: Optional[List[tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantAllowOrBlockListAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantAllowOrBlockListAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantAllowOrBlockListAction()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Specifies when the tenant allow-block-list expires in date time.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Specifies when the tenant allow-block-list expires in date time.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(tenant_allow_block_list_action.TenantAllowBlockListAction)),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult)),
        }
        return fields
    
    @property
    def note(self,) -> Optional[str]:
        """
        Gets the note property value. Specifies the note added to the tenant allow block list entry in the format of string.
        Returns: Optional[str]
        """
        return self._note
    
    @note.setter
    def note(self,value: Optional[str] = None) -> None:
        """
        Sets the note property value. Specifies the note added to the tenant allow block list entry in the format of string.
        Args:
            value: Value to set for the note property.
        """
        self._note = value
    
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
    def results(self,) -> Optional[List[tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult]]:
        """
        Gets the results property value. Contains the result of the submission that lead to the tenant allow-block-list entry creation.
        Returns: Optional[List[tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult]]
        """
        return self._results
    
    @results.setter
    def results(self,value: Optional[List[tenant_allow_block_list_entry_result.TenantAllowBlockListEntryResult]] = None) -> None:
        """
        Sets the results property value. Contains the result of the submission that lead to the tenant allow-block-list entry creation.
        Args:
            value: Value to set for the results property.
        """
        self._results = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("action", self.action)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("note", self.note)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

