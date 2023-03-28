from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class WipePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new wipePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The keepEnrollmentData property
        self._keep_enrollment_data: Optional[bool] = None
        # The keepUserData property
        self._keep_user_data: Optional[bool] = None
        # The macOsUnlockCode property
        self._mac_os_unlock_code: Optional[str] = None
        # The persistEsimDataPlan property
        self._persist_esim_data_plan: Optional[bool] = None
        # The useProtectedWipe property
        self._use_protected_wipe: Optional[bool] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WipePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WipePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WipePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "keepEnrollmentData": lambda n : setattr(self, 'keep_enrollment_data', n.get_bool_value()),
            "keepUserData": lambda n : setattr(self, 'keep_user_data', n.get_bool_value()),
            "macOsUnlockCode": lambda n : setattr(self, 'mac_os_unlock_code', n.get_str_value()),
            "persistEsimDataPlan": lambda n : setattr(self, 'persist_esim_data_plan', n.get_bool_value()),
            "useProtectedWipe": lambda n : setattr(self, 'use_protected_wipe', n.get_bool_value()),
        }
        return fields
    
    @property
    def keep_enrollment_data(self,) -> Optional[bool]:
        """
        Gets the keepEnrollmentData property value. The keepEnrollmentData property
        Returns: Optional[bool]
        """
        return self._keep_enrollment_data
    
    @keep_enrollment_data.setter
    def keep_enrollment_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the keepEnrollmentData property value. The keepEnrollmentData property
        Args:
            value: Value to set for the keep_enrollment_data property.
        """
        self._keep_enrollment_data = value
    
    @property
    def keep_user_data(self,) -> Optional[bool]:
        """
        Gets the keepUserData property value. The keepUserData property
        Returns: Optional[bool]
        """
        return self._keep_user_data
    
    @keep_user_data.setter
    def keep_user_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the keepUserData property value. The keepUserData property
        Args:
            value: Value to set for the keep_user_data property.
        """
        self._keep_user_data = value
    
    @property
    def mac_os_unlock_code(self,) -> Optional[str]:
        """
        Gets the macOsUnlockCode property value. The macOsUnlockCode property
        Returns: Optional[str]
        """
        return self._mac_os_unlock_code
    
    @mac_os_unlock_code.setter
    def mac_os_unlock_code(self,value: Optional[str] = None) -> None:
        """
        Sets the macOsUnlockCode property value. The macOsUnlockCode property
        Args:
            value: Value to set for the mac_os_unlock_code property.
        """
        self._mac_os_unlock_code = value
    
    @property
    def persist_esim_data_plan(self,) -> Optional[bool]:
        """
        Gets the persistEsimDataPlan property value. The persistEsimDataPlan property
        Returns: Optional[bool]
        """
        return self._persist_esim_data_plan
    
    @persist_esim_data_plan.setter
    def persist_esim_data_plan(self,value: Optional[bool] = None) -> None:
        """
        Sets the persistEsimDataPlan property value. The persistEsimDataPlan property
        Args:
            value: Value to set for the persist_esim_data_plan property.
        """
        self._persist_esim_data_plan = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("keepEnrollmentData", self.keep_enrollment_data)
        writer.write_bool_value("keepUserData", self.keep_user_data)
        writer.write_str_value("macOsUnlockCode", self.mac_os_unlock_code)
        writer.write_bool_value("persistEsimDataPlan", self.persist_esim_data_plan)
        writer.write_bool_value("useProtectedWipe", self.use_protected_wipe)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def use_protected_wipe(self,) -> Optional[bool]:
        """
        Gets the useProtectedWipe property value. The useProtectedWipe property
        Returns: Optional[bool]
        """
        return self._use_protected_wipe
    
    @use_protected_wipe.setter
    def use_protected_wipe(self,value: Optional[bool] = None) -> None:
        """
        Sets the useProtectedWipe property value. The useProtectedWipe property
        Args:
            value: Value to set for the use_protected_wipe property.
        """
        self._use_protected_wipe = value
    

