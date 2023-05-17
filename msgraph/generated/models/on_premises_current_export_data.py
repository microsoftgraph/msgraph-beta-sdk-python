from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class OnPremisesCurrentExportData(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesCurrentExportData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the onPremises client machine which ran the last export.
        self._client_machine_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The count of pending adds from on-premises directory.
        self._pending_objects_addition: Optional[int] = None
        # The count of pending deletes from on-premises directory.
        self._pending_objects_deletion: Optional[int] = None
        # The count of pending updates from on-premises directory.
        self._pending_objects_update: Optional[int] = None
        # The name of the dirsync service account which is configured to connect to the directory.
        self._service_account: Optional[str] = None
        # The count of updated links during the current directory sync export run.
        self._successful_links_provisioning_count: Optional[int] = None
        # The count of objects which were successfully provisioned during the current directory sync export run.
        self._successful_objects_provisioning_count: Optional[int] = None
        # The total number of objects in the AAD Connector Space.
        self._total_connector_space_objects: Optional[int] = None
    
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
    def client_machine_name(self,) -> Optional[str]:
        """
        Gets the clientMachineName property value. The name of the onPremises client machine which ran the last export.
        Returns: Optional[str]
        """
        return self._client_machine_name
    
    @client_machine_name.setter
    def client_machine_name(self,value: Optional[str] = None) -> None:
        """
        Sets the clientMachineName property value. The name of the onPremises client machine which ran the last export.
        Args:
            value: Value to set for the client_machine_name property.
        """
        self._client_machine_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesCurrentExportData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesCurrentExportData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesCurrentExportData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "clientMachineName": lambda n : setattr(self, 'client_machine_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pendingObjectsAddition": lambda n : setattr(self, 'pending_objects_addition', n.get_int_value()),
            "pendingObjectsDeletion": lambda n : setattr(self, 'pending_objects_deletion', n.get_int_value()),
            "pendingObjectsUpdate": lambda n : setattr(self, 'pending_objects_update', n.get_int_value()),
            "serviceAccount": lambda n : setattr(self, 'service_account', n.get_str_value()),
            "successfulLinksProvisioningCount": lambda n : setattr(self, 'successful_links_provisioning_count', n.get_int_value()),
            "successfulObjectsProvisioningCount": lambda n : setattr(self, 'successful_objects_provisioning_count', n.get_int_value()),
            "totalConnectorSpaceObjects": lambda n : setattr(self, 'total_connector_space_objects', n.get_int_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def pending_objects_addition(self,) -> Optional[int]:
        """
        Gets the pendingObjectsAddition property value. The count of pending adds from on-premises directory.
        Returns: Optional[int]
        """
        return self._pending_objects_addition
    
    @pending_objects_addition.setter
    def pending_objects_addition(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingObjectsAddition property value. The count of pending adds from on-premises directory.
        Args:
            value: Value to set for the pending_objects_addition property.
        """
        self._pending_objects_addition = value
    
    @property
    def pending_objects_deletion(self,) -> Optional[int]:
        """
        Gets the pendingObjectsDeletion property value. The count of pending deletes from on-premises directory.
        Returns: Optional[int]
        """
        return self._pending_objects_deletion
    
    @pending_objects_deletion.setter
    def pending_objects_deletion(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingObjectsDeletion property value. The count of pending deletes from on-premises directory.
        Args:
            value: Value to set for the pending_objects_deletion property.
        """
        self._pending_objects_deletion = value
    
    @property
    def pending_objects_update(self,) -> Optional[int]:
        """
        Gets the pendingObjectsUpdate property value. The count of pending updates from on-premises directory.
        Returns: Optional[int]
        """
        return self._pending_objects_update
    
    @pending_objects_update.setter
    def pending_objects_update(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingObjectsUpdate property value. The count of pending updates from on-premises directory.
        Args:
            value: Value to set for the pending_objects_update property.
        """
        self._pending_objects_update = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("clientMachineName", self.client_machine_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingObjectsAddition", self.pending_objects_addition)
        writer.write_int_value("pendingObjectsDeletion", self.pending_objects_deletion)
        writer.write_int_value("pendingObjectsUpdate", self.pending_objects_update)
        writer.write_str_value("serviceAccount", self.service_account)
        writer.write_int_value("successfulLinksProvisioningCount", self.successful_links_provisioning_count)
        writer.write_int_value("successfulObjectsProvisioningCount", self.successful_objects_provisioning_count)
        writer.write_int_value("totalConnectorSpaceObjects", self.total_connector_space_objects)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_account(self,) -> Optional[str]:
        """
        Gets the serviceAccount property value. The name of the dirsync service account which is configured to connect to the directory.
        Returns: Optional[str]
        """
        return self._service_account
    
    @service_account.setter
    def service_account(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceAccount property value. The name of the dirsync service account which is configured to connect to the directory.
        Args:
            value: Value to set for the service_account property.
        """
        self._service_account = value
    
    @property
    def successful_links_provisioning_count(self,) -> Optional[int]:
        """
        Gets the successfulLinksProvisioningCount property value. The count of updated links during the current directory sync export run.
        Returns: Optional[int]
        """
        return self._successful_links_provisioning_count
    
    @successful_links_provisioning_count.setter
    def successful_links_provisioning_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulLinksProvisioningCount property value. The count of updated links during the current directory sync export run.
        Args:
            value: Value to set for the successful_links_provisioning_count property.
        """
        self._successful_links_provisioning_count = value
    
    @property
    def successful_objects_provisioning_count(self,) -> Optional[int]:
        """
        Gets the successfulObjectsProvisioningCount property value. The count of objects which were successfully provisioned during the current directory sync export run.
        Returns: Optional[int]
        """
        return self._successful_objects_provisioning_count
    
    @successful_objects_provisioning_count.setter
    def successful_objects_provisioning_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulObjectsProvisioningCount property value. The count of objects which were successfully provisioned during the current directory sync export run.
        Args:
            value: Value to set for the successful_objects_provisioning_count property.
        """
        self._successful_objects_provisioning_count = value
    
    @property
    def total_connector_space_objects(self,) -> Optional[int]:
        """
        Gets the totalConnectorSpaceObjects property value. The total number of objects in the AAD Connector Space.
        Returns: Optional[int]
        """
        return self._total_connector_space_objects
    
    @total_connector_space_objects.setter
    def total_connector_space_objects(self,value: Optional[int] = None) -> None:
        """
        Sets the totalConnectorSpaceObjects property value. The total number of objects in the AAD Connector Space.
        Args:
            value: Value to set for the total_connector_space_objects property.
        """
        self._total_connector_space_objects = value
    

